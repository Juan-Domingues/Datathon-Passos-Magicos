import pandas as pd
import unicodedata
import re
from sklearn.impute import KNNImputer

def remover_acentos(texto):
    return unicodedata.normalize("NFKD", texto).encode("ASCII", "ignore").decode("ASCII")

def padronizar_colunas(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.upper()
        .map(remover_acentos)
        .str.replace(" ", "_")
    )
    return df

def extrair_fase(valor):
    if pd.isna(valor):
        return None
    
    valor = str(valor).upper()

    if "ALFA" in valor:
        return 0
    
    match = re.search(r"\d+", valor)
    
    if match:
        return int(match.group())
    
    return None


arquivo = "BASE DE DADOS PEDE 2024 - DATATHON.xlsx"

df_2022 = pd.read_excel(arquivo, sheet_name="PEDE2022")
df_2022 = padronizar_colunas(df_2022)

df_2022 = df_2022.rename(columns={
    "INDE_22": "INDE"
})

df_2022["ANO"] = 2022

# criar IPP vazio (não existe em 2022)
df_2022["IPP"] = None

colunas_final = [
    "RA","ANO","FASE","TURMA","GENERO","ANO_NASC","ANO_INGRESSO",
    "INSTITUICAO_DE_ENSINO","INDE","IAN","IDA","IEG","IAA","IPS",
    "IPP","IPV","MATEM","PORTUG","INGLES","DEFAS","FASE_IDEAL",
    "ATINGIU_PV","INDICADO"
]

df_2022 = df_2022[colunas_final]

df_2023 = pd.read_excel(arquivo, sheet_name="PEDE2023")
df_2023 = padronizar_colunas(df_2023)

df_2023 = df_2023.rename(columns={
    "INDE_23": "INDE",
    "INDE_2023": "INDE",
    "DATA_DE_NASC": "ANO_NASC",
    "MAT": "MATEM",
    "POR": "PORTUG",
    "ING": "INGLES",
    "DEFASAGEM": "DEFAS"
})

df_2023["ANO_NASC"] = pd.to_datetime(df_2023["ANO_NASC"], errors="coerce").dt.year
df_2023["ANO"] = 2023

df_2023 = df_2023.loc[:, ~df_2023.columns.duplicated()]

mapa_fases = {
    "ALFA":0,
    "FASE 1":1,
    "FASE 2":2,
    "FASE 3":3,
    "FASE 4":4,
    "FASE 5":5,
    "FASE 6":6,
    "FASE 7":7,
    "FASE 8":8
}

df_2023["FASE"] = df_2023["FASE"].map(mapa_fases)

df_2023["ATINGIU_PV"] = df_2023["ATINGIU_PV"].fillna(0)
df_2023["INDICADO"] = df_2023["INDICADO"].fillna(0)

df_2023 = df_2023[colunas_final]

df_2024 = pd.read_excel(arquivo, sheet_name="PEDE2024")
df_2024 = padronizar_colunas(df_2024)

df_2024 = df_2024.rename(columns={
    "INDE_2024": "INDE",
    "DATA_DE_NASC": "ANO_NASC",
    "MAT": "MATEM",
    "POR": "PORTUG",
    "ING": "INGLES",
    "DEFASAGEM": "DEFAS"
})

df_2024["ANO_NASC"] = pd.to_datetime(df_2024["ANO_NASC"], errors="coerce").dt.year
df_2024["ANO"] = 2024

df_2024 = df_2024.loc[:, ~df_2024.columns.duplicated()]

# corrigir FASE
df_2024["FASE"] = df_2024["FASE"].apply(extrair_fase)

df_2024 = df_2024[colunas_final]

# converter INDE para número
df_2024["INDE"] = pd.to_numeric(df_2024["INDE"], errors="coerce")

df_2022["IPP"] = df_2022["IPP"].astype(float)

dataset = pd.concat(
    [df_2022, df_2023, df_2024],
    ignore_index=True
)

# criar idade
dataset["IDADE"] = dataset["ANO"] - dataset["ANO_NASC"]

colunas_knn = [
    "IAN","IDA","IEG","IAA","IPS","IPV","IPP"
]

imputer = KNNImputer(n_neighbors=5)

dataset[colunas_knn] = imputer.fit_transform(
    dataset[colunas_knn]
)

dataset["INDE_CALCULADO"] = dataset[
    ["IAN","IDA","IEG","IAA","IPS","IPP","IPV"]
].mean(axis=1)

dataset["INDE"] = dataset["INDE"].fillna(dataset["INDE_CALCULADO"])

dataset["ATINGIU_PV"] = dataset["ATINGIU_PV"].replace({
    "Sim":1,
    "Não":0,
    "Nao":0
})
dataset["ATINGIU_PV"] = dataset["ATINGIU_PV"].fillna(0).astype(int)

dataset["INDICADO"] = dataset["INDICADO"].replace({
    "Sim":1,
    "Não":0,
    "Nao":0
})
dataset["INDICADO"] = dataset["INDICADO"].fillna(0).astype(int)

colunas_knn_inde = [
    "IAN","IDA","IEG","IAA","IPS","IPP","IPV","INDE"
]

imputer_inde = KNNImputer(n_neighbors=5)

dataset[colunas_knn_inde] = imputer_inde.fit_transform(
    dataset[colunas_knn_inde]
)

print("\nMissing INDE:")
print(dataset["INDE"].isna().sum())

dataset["GENERO"] = dataset["GENERO"].replace({
    "Menino":"Masculino",
    "Menina":"Feminino"
})


dataset = dataset.sort_values(["RA","ANO"])

dataset["FASE_PASSADA"] = dataset.groupby("RA")["FASE"].shift()

dataset["REPETENTE_FASE"] = (
    dataset["FASE"] == dataset["FASE_PASSADA"]
).astype(int)

dataset["REPETENTE_FASE"] = dataset["REPETENTE_FASE"].fillna(0)

def corrigir_indicador(valor):

    if pd.isna(valor):
        return valor

    valor = float(valor)

    # caso absurdo (erro de escala)
    if valor > 10:
        valor = valor / 1000000000

    return valor

indicadores = [
    "INDE","IAN","IDA","IEG","IAA","IPS","IPP","IPV"
]

for col in indicadores:
    dataset[col] = dataset[col].apply(corrigir_indicador)

dataset.drop(columns=["INDE_CALCULADO"], inplace=True)

dataset.to_csv(
    "dataset_pede_tratado.csv",
    index=False,
    encoding="utf-8"
)

dataset["IPV"] = dataset["IPV"].clip(lower=0)

print(dataset[indicadores].describe())
print("\nDataset salvo com sucesso!")