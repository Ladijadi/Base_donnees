import sqlite3

# Connexion à la base de données SQLite (création d'une base locale)
conn = sqlite3.connect('marketing.db')
cursor = conn.cursor()

# Création des tables avec les contraintes
cursor.execute('''
CREATE TABLE IF NOT EXISTS Client (
    Client_ID INTEGER PRIMARY KEY,
    Nom VARCHAR(255),
    Prenom VARCHAR(255),
    Email VARCHAR(255),
    Telephone TEXT,
    Date_Naissance DATE,
    Adresse TEXT,
    Consentement_Marketing BOOLEAN
);''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS Commande (
    Commande_ID INTEGER PRIMARY KEY,
    Date_Commande DATE,
    Montant_Commande REAL,
    Client_ID INTEGER,
    FOREIGN KEY (Client_ID) REFERENCES Client(Client_ID)
);''')

print("base de données create")

conn.commit()
conn.close()