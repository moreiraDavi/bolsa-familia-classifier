# Projeto: Classificação de Beneficiários do Bolsa Família

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![License](https://img.shields.io/badge/license-MIT-green)

Este projeto foi desenvolvido para que eu treinasse meus conhecimentos em Machine Learning utilizando Python e algumas bibliotecas

##  📊 Dados Utilizados

O dataset `Base_Simulada_Bolsa_Fam_lia.csv` foi gerado através de IA para fins didáticos e contem 200 registros simulados com as seguintes colonuas:
- `idade_responsavel`
- `renda_familiar`
- `numero_dependentes`
- `escolaridade_responsavel`
- `estado`
- `recebe_bolsa_familia` (variável-alvo)
- `nao_pagou`

## 🧠 Técnicas utilizadas

- Normalização de dados com `LabelEncoder`
- Visualização com `seaborn` (heatmap e boxplot)
- Divisão treino/teste com `train_test_split`
- Modelo: `DecisionTreeClassifier`
- Avaliação com `accuracy_score`, `classification_report` e `confusion_matrix`
- Função para aplicar o modelo a novos dados

## ⚙️ Como rodar o notebook

- https://github.com/moreiraDavi/bolsa-familia-classifier.git
- pip install pandas scikit-learn matplotlib seaborn jupyter
