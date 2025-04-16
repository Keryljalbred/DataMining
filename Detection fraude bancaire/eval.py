# evaluation.py

from sklearn.metrics import roc_auc_score, classification_report

def evaluate_models(models, X_test, y_test):
    for model in models:
        y_pred = model.predict(X_test)
        print(f"Model: {model.__class__.__name__}")
        print("ROC AUC:", roc_auc_score(y_test, y_pred))
        print("Classification Report:\n", classification_report(y_test, y_pred))