# preprocessing.py

import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = re.sub(r'@\w+|#\w+|http\S+|[^a-zA-Z\s]', '', text)
    text = text.lower()
    text = ' '.join(word for word in text.split() if word not in stop_words)
    return text

def preprocess_data(validation_data):
    # Utiliser l'index 3 pour accéder à la colonne contenant le texte des tweets
    validation_data['cleaned_text'] = validation_data[3].apply(clean_text)  
    return validation_data