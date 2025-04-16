# resampling.py

from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE

def resample_data(train_data):
    # Séparer les caractéristiques et la cible
    X = train_data.drop('is_fraud', axis=1)  # Supprimez la colonne cible
    y = train_data['is_fraud']  # Colonne cible

    # Ne garder que les colonnes numériques
    X = X.select_dtypes(include=['float64', 'int64', 'bool'])

    # Diviser les données en ensembles d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

    # Rééchantillonnage avec SMOTE
    smote = SMOTE(random_state=42)
    X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

    return X_train_resampled, y_train_resampled, X_test, y_test