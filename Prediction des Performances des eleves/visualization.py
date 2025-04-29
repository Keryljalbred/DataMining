import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

def visualize_results(y_test, y_pred):
    cm = confusion_matrix(y_test, y_pred)
    
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['0', '1', '2', '3', '4', '5', '6'], yticklabels=['0', '1', '2', '3', '4', '5', '6'])
    plt.title('Matrice de Confusion')
    plt.xlabel('Prédit')
    plt.ylabel('Réel')
    plt.savefig('matrice_confusion.png')  # Sauvegarder le graphique dans un fichier
    plt.close()