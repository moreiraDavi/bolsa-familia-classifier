import seaborn as sns
import matplotlib.pyplot as plt

def plot_heatmap_correlacao(df):
    plt.figure(figsize=(10,6))
    plt.title("Correlação entre variáveis")
    sns.heatmap(df.corr(), annot=True, cmap="Blues")
    plt.show()