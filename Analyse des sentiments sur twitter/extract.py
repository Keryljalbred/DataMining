# feature_extraction.py

from sklearn.feature_extraction.text import TfidfVectorizer

def extract_features(validation_data):
    vectorizer = TfidfVectorizer()
    X_val = vectorizer.fit_transform(validation_data[3])  # Utilisez l'index 3 pour le texte du tweet
    y_val = validation_data[2]  # Utilisez l'index 2 pour le sentiment
    return X_val, y_val