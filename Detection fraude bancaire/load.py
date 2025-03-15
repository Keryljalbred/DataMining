# data_loader.py

import pandas as pd

def load_data():
    # Charger les fichiers CSV
    train_data = pd.read_csv('fraudTrain.csv')  # Remplacez par le chemin correct
    test_data = pd.read_csv('fraudTest.csv')    # Remplacez par le chemin correct
    return train_data, test_data