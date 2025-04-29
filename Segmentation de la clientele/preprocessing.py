import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(file_path):
    # Charger les données
    df = pd.read_csv(file_path)

    # Vérifier les valeurs manquantes
    print(df.isnull().sum())

    # Encoder les variables catégorielles
    df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})

    # Sélectionner les caractéristiques pertinentes
    X = df[['Gender', 'Age', 'Annual Income (k$)', 'Spending Score (1-100)']]

    # Standardiser les données
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, df