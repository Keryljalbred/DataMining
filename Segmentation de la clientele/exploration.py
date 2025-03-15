import seaborn as sns
import matplotlib.pyplot as plt

def explore_data(df):
    # Visualiser la distribution des données
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='Annual Income (k$)', y='Spending Score (1-100)', hue='Gender')
    plt.title('Distribution des Clients par Revenu et Score de Dépense')
    plt.show()

    # Visualiser les corrélations
    plt.figure(figsize=(8, 6))
    sns.heatmap(df.corr(), annot=True, fmt=".2f")
    plt.title('Matrice de Corrélation')
    plt.show()