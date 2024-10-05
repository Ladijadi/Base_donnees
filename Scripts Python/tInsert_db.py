import sqlite3
import csv

# Chemins des fichiers CSV
client_csv_path = 'Data/Data_Marketing_client.csv'
commande_csv_path = 'Data/Data_Marketing_cmd.csv'

# Connexion à la base de données SQLite (création d'une base locale)
conn = sqlite3.connect('marketing.db')
cursor = conn.cursor()

# Insertion des donnÃ©es des clients
with open(client_csv_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        cursor.execute("""
            INSERT INTO Client (Client_ID, Nom, Prenom, Email, Telephone, Date_Naissance, Adresse, Consentement_Marketing)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            (row['Client_ID'], row['Nom'], row['Prenom'], row['Email'], row['Telephone'], row['Date_Naissance'], row['Adresse'], row['Consentement_Marketing'])
        )
with open(commande_csv_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        cursor.execute("""
            INSERT INTO Commande (Commande_ID, Client_ID, Montant_Commande, Date_Commande)
            VALUES (?, ?, ?, ?)""",
            (row['Commande_ID'], row['Client_ID'], row['Montant_Commande'], row['Date_Commande']
             ))
      
conn.commit()
conn.close()