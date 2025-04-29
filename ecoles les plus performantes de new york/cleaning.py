def clean_data(df):
    # Vérifier les valeurs manquantes
    print("Valeurs manquantes par colonne :")
    print(df.isnull().sum())

    # Supprimer les valeurs manquantes
    df.dropna(inplace=True)

    # Convertir les types de données si nécessaire
    df['average_math'] = df['average_math'].astype(int)

    return df