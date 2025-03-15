# preprocessing.py

import pandas as pd

def preprocess_data(data):
    # Nettoyage des données : gérer les valeurs manquantes, les doublons, etc.
    data = data.dropna()  # Supprimez les lignes avec des valeurs manquantes
    data = data.drop_duplicates()  # Supprimez les doublons
    
    # Convertir les colonnes pertinentes en type approprié
    data['trans_date_trans_time'] = pd.to_datetime(data['trans_date_trans_time'])

    # Extraire des caractéristiques à partir de la date
    data['trans_hour'] = data['trans_date_trans_time'].dt.hour
    data['trans_day'] = data['trans_date_trans_time'].dt.day
    data['trans_month'] = data['trans_date_trans_time'].dt.month
    data['trans_year'] = data['trans_date_trans_time'].dt.year
    data['trans_weekday'] = data['trans_date_trans_time'].dt.weekday

    # Supprimer la colonne d'origine si nécessaire
    data = data.drop('trans_date_trans_time', axis=1)

    # Encoder les variables catégorielles
    data = pd.get_dummies(data, columns=['category', 'gender', 'job'], drop_first=True)

    # Vérifiez le type des colonnes encodées
    print(data.dtypes)  # Ajoutez cette ligne pour vérifier les types de données
    print(data.head())  # Voir les premières lignes des données

    return data