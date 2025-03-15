import seaborn as sns
import matplotlib.pyplot as plt

def visualize_clusters(df):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='Annual Income (k$)', y='Spending Score (1-100)', hue='Cluster', palette='Set1')
    plt.title('Segments de Clientèle')
    plt.show()