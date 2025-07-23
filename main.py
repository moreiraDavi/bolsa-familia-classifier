from src.tratamento_dados import carregar_dados, codificar_colunas
from src.visualizacoes import plot_heatmap_correlacao
from src.modelo import separar_dados, treinar_modelo, avaliar_modelo

# Carregar e separar dados
df = carregar_dados(r"data/raw/Base_Simulada_Bolsa_Fam_lia.csv")
df = codificar_colunas(df, ["escolaridade_responsavel", "estado"])

# Visualizar Correlações
plot_heatmap_correlacao(df)

# Separar, treinar e avaliar
X_train, X_test, y_train, y_test = separar_dados(df, "recebe_bolsa_familia")
modelo = treinar_modelo(X_train, y_train)
avaliar_modelo(modelo, X_test, y_test)