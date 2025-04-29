import pandas as pd

def preprocess_data(df):
    # Suppression des valeurs manquantes
    df = df.dropna()
    
    # Encodage des variables catégorielles
    df = pd.get_dummies(df, drop_first=True)
    
    return df