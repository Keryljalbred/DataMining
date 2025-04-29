import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

def perform_apriori(transactions, min_support):
    """Calcule les itemsets fréquents en utilisant l'algorithme Apriori."""
    encoder = TransactionEncoder()
    onehot = encoder.fit(transactions).transform(transactions)  # Transforme les transactions
    onehot_df = pd.DataFrame(onehot, columns=encoder.columns_)  # Convertit en DataFrame
    
    # Calcule les itemsets fréquents
    frequent_itemsets = apriori(onehot_df, min_support=min_support, use_colnames=True)
    return frequent_itemsets

def generate_rules(frequent_itemsets, min_threshold):
    """Génère des règles d'association à partir des itemsets fréquents."""
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=min_threshold)
    return rules