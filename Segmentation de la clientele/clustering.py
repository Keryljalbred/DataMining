from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def kmeans_clustering(X_scaled, df):
    # Déterminer le nombre optimal de clusters
    inertia = []
    K = range(1, 11)
    for k in K:
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(X_scaled)
        inertia.append(kmeans.inertia_)

    plt.figure(figsize=(10, 6))
    plt.plot(K, inertia, marker='o')
    plt.title('Méthode du Coude')
    plt.xlabel('Nombre de Clusters')
    plt.ylabel('Inertie')
    plt.savefig('methode du coude.png')  # Sauvegarder le graphique dans un fichier
    plt.close()

    # Appliquer K-means avec le nombre optimal de clusters
    optimal_k = 5  # Ajustez selon le graphique
    kmeans = KMeans(n_clusters=optimal_k, random_state=42)
    df['Cluster'] = kmeans.fit_predict(X_scaled)

    return df