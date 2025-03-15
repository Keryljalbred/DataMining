# main.py

from load import load_data
from preprocessing import preprocess_data
from resampling import resample_data
from model import train_and_evaluate

def main():
    # Charger les données
    train_data, test_data = load_data()
    
    # Prétraiter les données
    train_data = preprocess_data(train_data)
    test_data = preprocess_data(test_data)
    
    # Rééchantillonner les données
    X_train, y_train, X_test, y_test = resample_data(train_data, test_data)
    
    # Entraîner et évaluer le modèle
    train_and_evaluate(X_train, y_train, X_test, y_test)

if __name__ == "__main__":
    main()