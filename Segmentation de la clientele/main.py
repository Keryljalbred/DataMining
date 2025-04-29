from preprocessing import preprocess_data
from exploration import explore_data
from clustering import kmeans_clustering
from visualization import visualize_clusters

def main():
    # Étape 1 : Prétraitement des données de shopping
    X_scaled, df = preprocess_data('Mall_Customers.csv')

    # Étape 2 : Analyse exploratoire
    explore_data(df)

    # Étape 3 : Regroupement K-means
    clustered_df = kmeans_clustering(X_scaled, df)

    # Étape 4 : Visualisation des résultats
    visualize_clusters(clustered_df)


if __name__ == "__main__":
    main()