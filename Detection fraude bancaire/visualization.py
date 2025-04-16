import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_fraud_distribution(data):
    plt.figure(figsize=(10, 6))
    sns.countplot(x='is_fraud', data=data)
    plt.title('Distribution des Fraudes')
    plt.xlabel('Fraude (0 = Non, 1 = Oui)')
    plt.ylabel('Nombre de Transactions')
    plt.savefig('fraud_distribution.png')
    plt.close()

def plot_transaction_amounts(data):
    plt.figure(figsize=(10, 6))
    sns.histplot(data[data['is_fraud'] == 0]['amt'], bins=50, color='blue', label='Non-Fraude', kde=True)
    sns.histplot(data[data['is_fraud'] == 1]['amt'], bins=50, color='red', label='Fraude', kde=True)
    plt.title('Montant des Transactions')
    plt.xlabel('Montant')
    plt.ylabel('Densité')
    plt.legend()
    plt.savefig('transaction_amounts.png')
    plt.close()

def plot_boxplot_transaction_amounts(data):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='is_fraud', y='amt', data=data)
    plt.title('Diagramme de Boîte des Montants des Transactions')
    plt.xlabel('Fraude (0 = Non, 1 = Oui)')
    plt.ylabel('Montant')
    plt.savefig('boxplot_transaction_amounts.png')
    plt.close()

def plot_correlation_matrix(data):
    plt.figure(figsize=(12, 8))
    # Gardez seulement les colonnes numériques
    numeric_data = data.select_dtypes(include=['number'])
    correlation = numeric_data.corr()
    sns.heatmap(correlation, annot=True, fmt=".2f", cmap='coolwarm', square=True)
    plt.title('Matrice de Corrélation')
    plt.savefig('correlation_matrix.png')
    plt.close()

def plot_age_distribution(data):
    # Assurez-vous que la colonne 'dob' est en datetime
    data['dob'] = pd.to_datetime(data['dob'])
    data['age'] = (pd.Timestamp.now() - data['dob']).dt.days // 365

    plt.figure(figsize=(10, 6))
    sns.histplot(data['age'], bins=30, kde=True, color='purple')
    plt.title('Distribution des Âges des Utilisateurs')
    plt.xlabel('Âge')
    plt.ylabel('Densité')
    plt.savefig('age_distribution.png')
    plt.close()