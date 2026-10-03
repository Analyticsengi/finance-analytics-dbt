import csv
import random
with open("ma_compta_sales.csv","w", newline="",encoding="utf-8") as file:
   writer = csv.writer(file,delimiter=";")
   writer.writerow(["Date", "Numéro de compte", "Libellé", "Centre de coût", "Mouvement", "Montant"])
   compte_vs_article={606:["ampoule","tondeuse","desinfectant"],
                       625:["hotel","restaurant","parking"],
                       612 :[ "voiture","camion", "photocopieur"],
                       218:[ "table de bureau", "ecran","armoire"]}
   centrescout=["Centre A","Centre B","Centre C","Centre D","Centre E"]
   deb_cred=["Débit","Crédit"]
   for i in range(500):
     compte=random.choice(list(compte_vs_article.keys ()))
     libel=random.choice(compte_vs_article.get(compte))
     centre=random.choice(centrescout)
     mouvement=random.choice(deb_cred)
     montant=round(random.uniform(0,1001),2)
     mois=random.randint(1,12)
     jour=random.randint(1,28)
     writer.writerow([f"{jour}/{mois}/2026", compte, libel, centre,mouvement, montant])

