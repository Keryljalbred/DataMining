import matplotlib.pyplot as plt
import seaborn as sns

def visualize_top_schools(top_schools):
    plt.figure(figsize=(10, 6))
    sns.barplot(x='average_math', y='school_name', data=top_schools)
    plt.title('Top 10 des écoles en mathématiques à New York')
    plt.xlabel('Score en mathématiques')
    plt.ylabel('Nom de l\'école')
    plt.savefig('top_schools.png')  # Sauvegarder le graphique dans un fichier
    plt.close()  # Fermer la figure pour libérer la mémoire

def visualize_neighborhood_scores(mean_scores_by_neighborhood):
    plt.figure(figsize=(12, 6))
    sns.barplot(x=mean_scores_by_neighborhood.index, y=mean_scores_by_neighborhood.values)
    plt.title('Moyenne des scores en mathématiques par quartier')
    plt.xlabel('Quartier')
    plt.ylabel('Score moyen')
    plt.savefig('Moyenne_quartier.png')  # Sauvegarder le graphique dans un fichier
    plt.close()