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
     writer.writerow(["01/01/2026", "610", "test", "Toulouse", "35", "40"])