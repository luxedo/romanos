"""Shhh respostas!"""
import pandas as pd

df_respostas = pd.read_csv("dados/answers.csv")
df_teste = pd.read_csv("dados/test.csv")
df_respostas["Name"] = df_respostas["Name"].str.replace("[()\"]", "")
df_teste["NameBackup"] = df_teste["Name"]
df_teste["Name"] = df_teste["Name"].str.replace("[()\"]", "")
df_merged = pd.merge(df_teste, df_respostas, on=["Name", "Age"], how="left")
df_merged = df_merged[["PassengerId", "Survived"]]
df_merged = df_merged.rename(columns={"Survived": "Never going to match me!"})


def verificar_respostas(df_previsoes, coluna_respostas):
    "Not meant to be organized"
    matches = pd.merge(
        df_merged, df_previsoes, on="PassengerId", how="left")[
            ["Never going to match me!", coluna_respostas]
        ]
    return (matches["Never going to match me!"] == matches[coluna_respostas]).sum()/len(matches)

