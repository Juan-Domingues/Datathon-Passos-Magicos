import streamlit as st
import pandas as pd
import numpy as np
import joblib
from pathlib import Path
import plotly.express as px

st.set_page_config(
    page_title="Predição de Defasagem Escolar",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent.parent

dataset_path = BASE_DIR / "dataset_pede_tratado.csv"
model_path = BASE_DIR / "modelo_risco_temporal_final.pkl"
df = pd.read_csv(dataset_path)
modelo = joblib.load(model_path)

df = df.sort_values(["RA","ANO"])

df["TEMPO_PROGRAMA"] = df["ANO"] - df["ANO_INGRESSO"]

for col in ["IDA","IEG","IAA","IPS","IPP","IPV"]:
    
    df[f"DELTA_{col}"] = (
        df.groupby("RA")[col]
        .diff()
        .fillna(0)
    )

df["FASE_PASSADA"] = df.groupby("RA")["FASE"].shift()

df["REPETENTE_FASE"] = (
    df["FASE"] == df["FASE_PASSADA"]
).astype(int)

df["REPETENTE_FASE"] = df["REPETENTE_FASE"].fillna(0)

df.drop(columns=["FASE_PASSADA"], inplace=True)

features_modelo = [
    "IDA","IEG","IAA","IPS","IPP","IPV",
    "IDADE","FASE","TEMPO_PROGRAMA","REPETENTE_FASE",
    "DELTA_IDA","DELTA_IEG","DELTA_IAA",
    "DELTA_IPS","DELTA_IPP","DELTA_IPV"
]

st.title("🎓 Predição de Risco de Defasagem Escolar")

st.info(
"""
Esta aplicação utiliza **Machine Learning** para identificar alunos com maior risco
de entrar em **defasagem escolar** no programa Passos Mágicos.

Ela também permite **simular cenários pedagógicos** para apoiar decisões educacionais.
"""
)

tab1, tab2, tab3 = st.tabs([
    "📊 Visão do Programa",
    "🎯 Previsão de Risco",
    "🧪 Simulação Pedagógica"
])

with tab1:

    st.header("📊 Panorama do Programa")

    total = len(df)

    df["PROB_RISCO"] = modelo.predict_proba(
        df[features_modelo].fillna(0)
    )[:,1]

    alto_risco = (df["PROB_RISCO"] > 0.6).sum()

    risco_medio = df["PROB_RISCO"].mean()

    c1,c2,c3 = st.columns(3)

    c1.metric("Total de registros", total)
    c2.metric("Alunos em alto risco", alto_risco)
    c3.metric("Risco médio", f"{risco_medio:.2%}")

    st.subheader("🚨 Alunos com maior risco")

    ano_atual = df["ANO"].max()

    ranking = df[df["ANO"] == ano_atual][
        ["RA","PROB_RISCO"]
    ].sort_values(
        "PROB_RISCO",
        ascending=False
    ).head(10)

    st.dataframe(ranking)

with tab2:

    st.header("🎯 Diagnóstico do Aluno")

    aluno = st.selectbox(
        "Selecione o aluno",
        df["RA"].unique()
    )

    dados_aluno = df[df["RA"] == aluno].sort_values("ANO")

    col1, col2 = st.columns([10,1])

    with col1:
        st.subheader("Histórico do aluno")

    with col2:
        with st.popover("ℹ️"):
        
            st.markdown("### Dicionário de Indicadores")

            dicionario = {
                "INDE":"Índice de Desempenho Educacional",
                "IAN":"Indicador de Adequação de Nível",
                "IDA":"Indicador de Desempenho Acadêmico",
                "IEG":"Indicador de Engajamento",
                "IAA":"Indicador de Autoavaliação",
                "IPS":"Indicador Psicossocial",
                "IPP":"Indicador Psicopedagógico",
                "IPV":"Indicador de Ponto de Virada"
            }

            dict_df = pd.DataFrame(
                dicionario.items(),
                columns=["Indicador","Descrição"]
            )

            st.table(dict_df)

    st.dataframe(dados_aluno)

    ultimo = dados_aluno.iloc[-1]

    entrada = ultimo[features_modelo].values.reshape(1,-1)

    prob = modelo.predict_proba(entrada)[0][1]

    st.subheader("Probabilidade de risco")

    st.metric(
        "Risco estimado",
        f"{prob:.2%}"
    )

    if prob < 0.3:

        st.success("🟢 Baixo risco")

    elif prob < 0.6:

        st.warning("🟡 Risco moderado")

    else:

        st.error("🔴 Alto risco")

with tab3:

    st.header("🧪 Simulação de Indicadores")

    st.write(
    """
    Ajuste os indicadores abaixo para simular intervenções pedagógicas
    e observar como o risco do aluno pode mudar.
    """
    )

    col1,col2,col3 = st.columns(3)

    with col1:

        ida = st.slider("IDA - Desempenho Acadêmico",0.0,10.0,6.0)

        ieg = st.slider("IEG - Engajamento",0.0,10.0,7.0)

    with col2:

        iaa = st.slider("IAA - Autoavaliação",0.0,10.0,7.0)

        ips = st.slider("IPS - Indicador Psicossocial",0.0,10.0,6.0)

    with col3:

        ipp = st.slider("IPP - Indicador Psicopedagógico",0.0,10.0,7.0)

        ipv = st.slider("IPV - Ponto de Virada",0.0,10.0,7.0)

    idade = st.slider("Idade",7,22,12)

    fase = st.slider("Fase do programa",0,8,3)

    tempo_programa = st.slider("Tempo no programa",0,10,3)

    repetente = st.selectbox(
        "Repetente na fase",
        [0,1],
        format_func=lambda x: "Não" if x==0 else "Sim"
    )

    st.caption("Observação: 0 = Não | 1 = Sim")

    entrada = pd.DataFrame([{
        "IDA": ida,
        "IEG": ieg,
        "IAA": iaa,
        "IPS": ips,
        "IPP": ipp,
        "IPV": ipv,
        "IDADE": idade,
        "FASE": fase,
        "TEMPO_PROGRAMA": tempo_programa,
        "REPETENTE_FASE": repetente,
        "DELTA_IDA":0,
        "DELTA_IEG":0,
        "DELTA_IAA":0,
        "DELTA_IPS":0,
        "DELTA_IPP":0,
        "DELTA_IPV":0
    }])

    prob = modelo.predict_proba(entrada)[0][1]

    st.metric(
        "Risco estimado",
        f"{prob:.2%}"
    )

