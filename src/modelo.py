from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Separa os dados em treinamento e teste
def separar_dados(df, coluna_alvo, test_size=0.3, random_state=42):
    X = df.drop(coluna_alvo, axis=1)
    y = df[coluna_alvo]
    return train_test_split(X,y, test_size=test_size, random_state=random_state)

# Treina o modelo
def treinar_modelo(X_train, y_train):
    modelo = RandomForestClassifier()
    modelo.fit(X_train,y_train)
    return modelo

# Avalia o modelo e imprime métricas
def avaliar_modelo(modelo, X_test,y_test):
    y_pred = modelo.predict(X_test)
    print("Acurácia:", accuracy_score(y_test,y_pred))
    print("Matriz Confusão:\n", confusion_matrix(y_test, y_pred))
    print("Relatório de Classificação:\n", classification_report(y_test, y_pred))