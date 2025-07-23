import pandas as pd

def carregar_dados(caminho_arquivo):
    return pd.read_csv(caminho_arquivo)


from sklearn.preprocessing import LabelEncoder

def codificar_colunas(df, colunas):
    for coluna in colunas:
        le = LabelEncoder()
        df[coluna] = le.fit_transform(df[coluna])
    return df