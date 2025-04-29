import pandas as pd
from load import load_data
from preprocessing import preprocess_data
from analysis import perform_apriori, generate_rules
from vizualization import plot_frequent_itemsets, plot_rules, plot_correlation_matrix

def main():
    # Charger le jeu de données
    data = load_data('Assignment-1_Data.csv')
    # Prétraiter les données
    transactions = preprocess_data(data)
    
    # Effectuer l'analyse Apriori
    frequent_itemsets = perform_apriori(transactions, min_support=0.01)
    print("Itemsets fréquents :")
    print(frequent_itemsets)

    # Visualiser les itemsets fréquents
    plot_frequent_itemsets(frequent_itemsets)

    # Générer des règles d'association
    rules = generate_rules(frequent_itemsets, min_threshold=0.5)
    print("\nRègles d'association :")
    print(rules)

    # Visualiser les règles d'association
    plot_rules(rules)

    # Visualiser la matrice de corrélation
    plot_correlation_matrix(data)

if __name__ == "__main__":
    main()