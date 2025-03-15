# data_loader.py

import pandas as pd

def load_data():
    # Charger le fichier CSV sans en-tête
    validation_data = pd.read_csv('twitter_validation.csv', header=None)
    
    # Afficher les colonnes pour voir ce qui a été chargé
    print("Colonnes de données de validation:", validation_data.columns)
    
    return validation_data