import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

df = pd.read_csv("dataset_pede_tratado.csv")

#Distribuição de alunos por ano

df["ANO"].value_counts().sort_index().plot(kind="bar")

plt.title("Quantidade de alunos por ano")
plt.xlabel("Ano")
plt.ylabel("Quantidade")
plt.show()

#Distribuição por fase

plt.figure(figsize=(8,5))

sns.countplot(data=df, x="FASE")

plt.title("Distribuição de alunos por fase")
plt.show()

#Distribuição da defasagem

plt.figure(figsize=(8,5))

sns.histplot(df["DEFAS"], bins=15)

plt.title("Distribuição da defasagem educacional")
plt.show()

#Evolução do INDE ao longo dos anos

inde_ano = df.groupby("ANO")["INDE"].mean()

inde_ano.plot(marker="o")

plt.title("Evolução média do INDE ao longo dos anos")
plt.ylabel("INDE médio")
plt.show()

#Relação entre engajamento e desempenho

plt.figure(figsize=(8,6))

sns.scatterplot(data=df, x="IEG", y="IDA", alpha=0.4)

plt.title("Engajamento vs Desempenho Acadêmico")
plt.show()

#Relação entre IPV e desempenho

plt.figure(figsize=(8,6))

sns.scatterplot(data=df, x="IPV", y="INDE", alpha=0.4)

plt.title("IPV vs INDE")
plt.show()

#Correlação entre indicadores

plt.figure(figsize=(10,8))

corr = df[
    ["INDE","IAN","IDA","IEG","IAA","IPS","IPP","IPV"]
].corr()

sns.heatmap(corr, annot=True, cmap="coolwarm")

plt.title("Correlação entre indicadores educacionais")
plt.show()

#Evolução do mesmo aluno (análise longitudinal)
alunos_multiplos = df.groupby("RA").size()

alunos_multiplos = alunos_multiplos[alunos_multiplos > 1]

print(alunos_multiplos.head())

ra_exemplo = alunos_multiplos.index[0]

exemplo = df[df["RA"] == "RA-1"].sort_values("ANO")

plt.figure(figsize=(6,4))

plt.plot(exemplo["ANO"], exemplo["INDE"], marker="o")

plt.title("Evolução do INDE - RA-1")
plt.xlabel("Ano")
plt.ylabel("INDE")

plt.show()

