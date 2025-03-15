# resampling.py

from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE

def resample_data(train_data, test_data):
    # Séparer les caractéristiques et la cible
    X = train_data.drop('is_fraud', axis=1)  # Supprimez la colonne cible
    y = train_data['is_fraud']  # Colonne cible
    
    # Diviser les données en ensembles d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
    
    # Vérifiez les types de données de X_train
    print("Types de données avant SMOTE :")
    print(X_train.dtypes)

    # Rééchantillonnage avec SMOTE
    smote = SMOTE(random_state=42)
    X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)
    
    # Préparer les données de test
    X_test_final = test_data.drop('is_fraud', axis=1)
    y_test_final = test_data['is_fraud']

    return X_train_resampled, y_train_resampled, X_test_final, y_test_final