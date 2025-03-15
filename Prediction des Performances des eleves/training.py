from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, classification_report

def train_model(df):
    # Sélection des caractéristiques et de la cible
    X = df.drop('G3', axis=1)  # Remplacez 'G3' par la colonne cible
    y = df['G3']  # Cible

    # Diviser les données en ensembles d'entraînement et de test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Entraînement du modèle
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    # Prédictions
    y_pred = model.predict(X_test)

    return y_test, y_pred