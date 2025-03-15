# model.py

from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import roc_auc_score, classification_report

def train_and_evaluate(X_train, y_train, X_test, y_test):
    # Entraîner un modèle de forêt aléatoire
    rf_model = RandomForestClassifier(random_state=42)
    rf_model.fit(X_train, y_train)
    y_pred_rf = rf_model.predict(X_test)
    
    # Entraîner un modèle XGBoost
    xgb_model = XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42)
    xgb_model.fit(X_train, y_train)
    y_pred_xgb = xgb_model.predict(X_test)
    
    # Évaluer les modèles
    print("Forêt Aléatoire:")
    print("ROC AUC:", roc_auc_score(y_test, y_pred_rf))
    print("Classification Report:\n", classification_report(y_test, y_pred_rf))
    
    print("XGBoost:")
    print("ROC AUC:", roc_auc_score(y_test, y_pred_xgb))
    print("Classification Report:\n", classification_report(y_test, y_pred_xgb))