import csv 
# chargement du fichier csv en utilisant la biblio csv 
with open(
     encoding=’utf-8’) as f:
    #lecture de la première ligne du fichier 5
    premiere_ligne = f.readline()
    #affichage d’une phrase puis de la première ligne du fichier 7
    print("Les descripteurs de la collection des établissements scolaires :") 
    print(premiere_ligne) 
    #les lignes suivantes permettent de connaître le format du fichier (utile pour les fichiers récupérés sur Internet) 
    dialecte_fichier_csv = csv.Sniffer().sniff(premiere_ligne) 
    #récupération des données du fichiers. 
    data_lignes = list(csv.reader(f, dialect=dialecte_fichier_csv)) 
    # data_lignes est une liste qui contient l’ensemble des données 
    # du fichier sans les descripteurs (premier élément à 0) 
    #print(data_lignes[0]
    #for el in data_lignes :
    nb_etab=0
    s=input("quelle ville/village recherchée")
    #mettre en majuscule
    s=s.upper()
    for el in data_lignes: 
        if s in el [9]:
            print(el[1],el[5])
            nb_etab=nb_etab+1
print("il y a ",nb_etab,"etablissement a", s)
