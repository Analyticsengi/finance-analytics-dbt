import csv
import random
with open("ma_compta_sales.csv","w", newline="",encoding="utf-8") as file:
   writer = csv.writer(file,delimiter=";")
   writer.writerow(["date", "numéro de compte", "libellé", "centre de coût", "débit", "crédit"])
   compte_vs_article={606:["ampoule","tondeuse","desinfectant"],
                       625:["hotel","restaurant","parking"],
                       612 :[ "voiture","camion", "photocopieur"],
                       218:[ "table de bureau", "ecran","armoire"]}
   for i in range(500):
     compte=random.choice(list(compte_vs_article.keys ()))
     libel=random.choice(compte_vs_article.get(compte))
     writer.writerow(["01/01/2026", compte, libel, "Toulouse", "35", "40"])

