from collection import collect_data
from data_processing import preprocess_data
from exploratory import explore_data
from training import train_model
from visualization import visualize_results
import matplotlib
matplotlib.use('Agg')  # Utiliser un backend non interactif
import matplotlib.pyplot as plt

def main():
    # Étape 1 : Collecte des données
    file_path_mat = 'student-mat.csv'  # Remplacez par le chemin du fichier CSV
    file_path_por = 'student-por.csv'  # Remplacez par le chemin du fichier CSV
    
    df_mat = collect_data(file_path_mat)
    df_por = collect_data(file_path_por)
    
    # Étape 2 : Prétraitement des données
    df_mat = preprocess_data(df_mat)
    df_por = preprocess_data(df_por)
    
    # Étape 3 : Exploration des données
    explore_data(df_mat)  # Exploration du premier fichier
    explore_data(df_por)  # Exploration du second fichier
    
    # Étape 4 : Formation du modèle
    y_test_mat, y_pred_mat = train_model(df_mat)
    y_test_por, y_pred_por = train_model(df_por)
    
    # Étape 5 : Visualisation des résultats
    visualize_results(y_test_mat, y_pred_mat)  # Visualisation pour le premier fichier
    visualize_results(y_test_por, y_pred_por)  # Visualisation pour le second fichier

if __name__ == "__main__":
    main()