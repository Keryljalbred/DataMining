import pandas as pd

def preprocess_data(data):
    """Prétraiter les données : gérer les valeurs manquantes et encoder la variable cible."""
    # Vérifier les valeurs manquantes
    if data.isnull().sum().any():
        data = data.dropna()  # Ou utilisez une autre méthode de traitement des NaN

    # Encodage de la variable cible (culture)
    data['crop'] = data['crop'].astype('category').cat.codes
    return data