import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.naive_bayes import MultinomialNB
import seaborn as sns
import pandas as pd

def train_and_evaluate(X_val, y_val):
    model = MultinomialNB()
    model.fit(X_val, y_val)  # Entraînement sur les données de validation

    y_val_pred = model.predict(X_val)

    # Calculer la matrice de confusion
    cm = confusion_matrix(y_val, y_val_pred)

    # Tracer la matrice de confusion
    plt.figure(figsize=(10, 7))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Classe 0', 'Classe 1'], yticklabels=['Classe 0', 'Classe 1'])
    plt.title('Matrice de Confusion')
    plt.xlabel('Prédictions')
    plt.ylabel('Vérités')
    
    # Enregistrer la matrice de confusion sous forme de PNG
    plt.savefig('confusion_matrix.png')
    plt.close()  # Fermer la figure pour éviter de l'afficher

    # Calculer et enregistrer le rapport de classification
    report = classification_report(y_val, y_val_pred, output_dict=True)
    report_df = pd.DataFrame(report).transpose()

    plt.figure(figsize=(10, 7))
    sns.heatmap(report_df.iloc[:-1, :-1], annot=True, fmt='.2f', cmap='Blues')
    plt.title('Rapport de Classification')
    plt.xlabel('Métriques')
    plt.ylabel('Classes')
    
    # Enregistrer le rapport de classification sous forme de PNG
    plt.savefig('classification_report.png')
    plt.close()  # Fermer la figure pour éviter de l'afficher

    print("Confusion Matrix:")
    print(cm)
    print("\nClassification Report:")
    print(report_df)