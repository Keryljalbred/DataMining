from loading import load_data
from cleaning import clean_data
from exploration import explore_data
from top_schools import get_top_schools
from visualization import visualize_top_schools, visualize_neighborhood_scores

import matplotlib
matplotlib.use('Agg')  # Utiliser un backend non interactif
import matplotlib.pyplot as plt

def main():
    # Chargement des données
    file_path = 'schools.csv'
    df = load_data(file_path)

    # Nettoyage des données
    df = clean_data(df)

    # Exploration des données
    mean_scores_by_neighborhood = explore_data(df)

    # Identification des écoles les plus performantes
    top_schools = get_top_schools(df)

    # Visualisation des résultats
    visualize_top_schools(top_schools)
    visualize_neighborhood_scores(mean_scores_by_neighborhood)

    # Affichage des écoles les plus performantes
    print("Les 10 écoles les plus performantes en mathématiques :")
    print(top_schools)

if __name__ == "__main__":
    main()