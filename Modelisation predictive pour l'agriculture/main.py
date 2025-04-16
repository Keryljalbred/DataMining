import pandas as pd
from load import load_data
from preprocessing import preprocess_data
from selection import plot_correlation_matrix, get_feature_importance
from model import train_and_evaluate_model

def main():
    # Charger le jeu de données
    data = load_data('soil_measures.csv')
    
    # Prétraiter les données
    data = preprocess_data(data)
    
    # Visualiser la matrice de corrélation
    plot_correlation_matrix(data)
    
    # Entraîner et évaluer le modèle
    model, feature_names = train_and_evaluate_model(data)

    # Afficher l'importance des caractéristiques
    importance_df = get_feature_importance(model, feature_names)
    print("\nImportance des caractéristiques :")
    print(importance_df)

if __name__ == "__main__":
    main()