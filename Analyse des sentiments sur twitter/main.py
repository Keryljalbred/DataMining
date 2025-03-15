# main.py

from load import load_data
from preprocess import preprocess_data
from extract import extract_features
from model import train_and_evaluate
from visualization import visualize_results

def main():
    # Charger les données de validation
    validation_data = load_data()
    validation_data = preprocess_data(validation_data)
    X_val, y_val = extract_features(validation_data)
    train_and_evaluate(X_val, y_val)
    visualize_results(validation_data)

if __name__ == "__main__":
    main()