def preprocess_data(data):
    """Prétraiter les données pour l'analyse des transactions."""
    data.columns = data.columns.str.strip()
    
    # Convertir Itemname en string
    data['Itemname'] = data['Itemname'].astype(str).str.strip()
    
    # Regrouper par 'BillNo' et appliquer sur 'Itemname'
    transactions = data.groupby(['BillNo'])['Itemname'].apply(list).tolist()
    return transactions