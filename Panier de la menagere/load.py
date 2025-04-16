import pandas as pd

def load_data(file_path):
    """Charge le jeu de données à partir d'un fichier CSV."""
    data = pd.read_csv(file_path, delimiter=';', on_bad_lines='skip', low_memory=False, dtype={'BillNo': str})
    
    # Conversion des colonnes
    data['Price'] = pd.to_numeric(data['Price'], errors='coerce')  # Convertit en numérique
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce')  #
    return data