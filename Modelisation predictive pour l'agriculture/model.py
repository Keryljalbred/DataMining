from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

def train_and_evaluate_model(data):
    """Entraîne et évalue le modèle Random Forest."""
    # Séparer les caractéristiques et la cible
    X = data[['N', 'P', 'K', 'ph']]
    y = data['crop']

    # Diviser les données
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Entraîner le modèle
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Prédictions
    y_pred = model.predict(X_test)

    # Évaluer le modèle
    print(classification_report(y_test, y_pred))
    print("Accuracy:", accuracy_score(y_test, y_pred))

    return model, X.columns