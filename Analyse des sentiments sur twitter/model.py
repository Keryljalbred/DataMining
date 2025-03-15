# model.py

from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix

def train_and_evaluate(X_val, y_val):
    model = MultinomialNB()
    model.fit(X_val, y_val)  # Notez que ici, vous n'avez pas d'ensemble d'entraînement, vous pouvez utiliser directement le modèle sur les données de validation

    y_val_pred = model.predict(X_val)

    print("Confusion Matrix:")
    print(confusion_matrix(y_val, y_val_pred))
    print("\nClassification Report:")
    print(classification_report(y_val, y_val_pred))