import pandas as pd

def load_data(file_path):
    """Charge le jeu de données à partir d'un fichier CSV."""
    data = pd.read_csv(file_path)
    return data