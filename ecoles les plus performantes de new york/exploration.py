import matplotlib.pyplot as plt
import seaborn as sns

def explore_data(df):
    # Statistiques descriptives
    print(df.describe())

    # Distribution des scores en mathématiques
    plt.figure(figsize=(10, 6))
    sns.histplot(df['average_math'], bins=20, kde=True)
    plt.title('Distribution des scores en mathématiques')
    plt.xlabel('Score')
    plt.savefig('distribution_score.png')  # Sauvegarder le graphique dans un fichier
    plt.close()

    # Moyenne des scores par quartier
    mean_scores_by_neighborhood = df.groupby('building_code')['average_math'].mean().sort_values(ascending=False)
    print(mean_scores_by_neighborhood)

    return mean_scores_by_neighborhood