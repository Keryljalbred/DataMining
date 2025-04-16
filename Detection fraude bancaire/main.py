# main.py

from load import load_data
from preprocessing import preprocess_data
from resampling import resample_data
from model import train_models
from eval import evaluate_models
from visualization import (
   plot_fraud_distribution,
    plot_transaction_amounts,
    plot_boxplot_transaction_amounts,
    plot_correlation_matrix,
    plot_age_distribution
)

def main():
    # Charger les données
    train_data, test_data = load_data()
    
    # Prétraiter les données
    train_data = preprocess_data(train_data)
    test_data = preprocess_data(test_data)
    
    # Générer des diagrammes
    plot_fraud_distribution(train_data)
    plot_transaction_amounts(train_data)
    plot_boxplot_transaction_amounts(train_data)
    plot_correlation_matrix(train_data)
    plot_age_distribution(train_data)
    
    # Échantillonnez un sous-ensemble des données pour un entraînement plus rapide
    train_data_sample = train_data.sample(frac=0.5, random_state=42)  # Prendre 50% des données
    
    # Rééchantillonner les données
    X_train, y_train, X_test, y_test = resample_data(train_data_sample)
    
    # Entraîner les modèles
    rf_model, xgb_model = train_models(X_train, y_train)
    
    # Évaluer les modèles
    evaluate_models([rf_model, xgb_model], X_test, y_test)

if __name__ == "__main__":
    main()