import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_frequent_itemsets(frequent_itemsets):
    """Trace les itemsets fréquents."""
    plt.figure(figsize=(10, 6))
    sns.barplot(x='support', y='itemsets', data=frequent_itemsets.sort_values('support', ascending=False).head(10), palette='Blues')
    plt.title('Top 10 des Itemsets Fréquents')
    plt.xlabel('Support')
    plt.ylabel('Itemsets')
    plt.savefig('frequent_itemsets.png')
    plt.close()

def plot_rules(rules):
    """Trace les règles d'association selon le lift."""
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='support', y='lift', size='confidence', sizes=(20, 200), data=rules)
    plt.title('Règles d\'Association')
    plt.xlabel('Support')
    plt.ylabel('Lift')
    plt.savefig('association_rules.png')
    plt.close()

def plot_correlation_matrix(data):
    """Trace la matrice de corrélation pour les colonnes numériques."""
    numeric_data = data.select_dtypes(include=['number'])  # Sélectionner uniquement les colonnes numériques
    correlation_matrix = numeric_data.corr()
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True)
    plt.title('Matrice de Corrélation')
    plt.show()