import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_correlation_matrix(data):
    """Trace la matrice de corrélation des caractéristiques."""
    correlation_matrix = data.corr()
    sns.heatmap(correlation_matrix, annot=True)
    plt.title('Matrice de Corrélation')
    plt.show()
    
def get_feature_importance(model, feature_names):
    """Retourne l'importance des caractéristiques du modèle."""
    importances = model.feature_importances_
    return pd.DataFrame(importances, index=feature_names, columns=['Importance']).sort_values('Importance', ascending=False)