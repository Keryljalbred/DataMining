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

    # Limiter le nombre de catégories dans les colonnes avec une haute cardinalité
    frequent_categories = data['merchant'].value_counts().nlargest(10).index
    data['merchant'] = data['merchant'].where(data['merchant'].isin(frequent_categories), 'Other')

    # Encoder les variables catégorielles (en évitant les grandes cardinalités)
    categorical_cols = ['merchant']
    data = pd.get_dummies(data, drop_first=True, columns=categorical_cols)

    return data