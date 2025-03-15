# visualization.py

import matplotlib.pyplot as plt
import seaborn as sns

def visualize_results(validation_data):
    sns.countplot(x=validation_data[2])
    plt.title('Distribution des Sentiments dans l\'Ensemble de Validation')
    plt.xlabel('Sentiment')
    plt.ylabel('Nombre de Tweets')
    plt.show()