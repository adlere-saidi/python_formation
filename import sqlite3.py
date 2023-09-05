import sqlite3

# Créer une connexion à la base de données
conn = sqlite3.connect("ma_base.db")
# Créer un curseur pour exécuter des commandes SQL
cur = conn.cursor()
# Créer la table chien avec 3 attributs
cur.execute("CREATE TABLE chien (sexe TEXT, couleur TEXT, nom TEXT)")

# Insérer 2 exemples de chiens dans la table
cur.execute("INSERT INTO chien VALUES ('Mâle', 'Noir', 'Rex')")
cur.execute("INSERT INTO chien VALUES ('Femelle', 'Blanc', 'Lila')")

# Valider les changements
conn.commit()

# Requêter l'ensemble des enregistrements de la table
cur.execute("SELECT * FROM chien")
rows = cur.fetchall()
print(rows)
# Afficher les résultats
#for row in rows:
#    print(row)

# Fermer la connexion
conn.close()