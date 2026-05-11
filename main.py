import csv 
# chargement du fichier csv en utilisant la biblio csv
#ouverture du fichier region 
with open("departement.csv", "r", encoding="utf-8") as f:
  dialecte_fichier_csv = csv.Sniffer().sniff(f.readline()) 
  datas_departement = list(csv.reader(f, dialect=dialecte_fichier_csv))
#ouverture du fichier communes
with open("communes_csv", "r", encoding="utf-8") as f:
  dialecte_fichier_csv = csv.Sniffer().sniff(f.readline())
  datas_communes = list(csv.reader(f, dialect=dialecte_fichier_csv))
print("Les departement avec le nom de leur chefs-lieux de departement")
#parcours de toutes les communes
for commune in datas_communes:
  #pour chaque communes, on parcours chaque région 16
  for dep in datas_departement:
    #si la commune est un chef lieu de région 18
    if commune[1]==region[2]:
      #affichier la ligne nom de région : nom de commune 20
     print(dep[4], " : ", commune[4])