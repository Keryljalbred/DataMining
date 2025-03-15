import seaborn as sns
import matplotlib.pyplot as plt

def explore_data(df):
    plt.figure(figsize=(10, 6))
    sns.histplot(df['G3'], bins=10)
    plt.title('Prediction des performances des eleves')
    plt.xlabel('Moyennes')
    plt.ylabel('Nombres d\'eleves')
    plt.savefig('distribution_g3.png')  # Sauvegarder le graphique dans un fichier
    plt.close()  # Fermer la figure pour libérer la mémoire