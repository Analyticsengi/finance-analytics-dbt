import csv
with open("ma_compta_sales.csv","w", newline="",encoding="utf-8") as file:
   writer = csv.writer(file,delimiter=";")
   writer.writerow(["date", "numéro de compte", "libellé", "centre de coût", "débit", "crédit"])
   for i in range(500):
     writer.writerow(["01/01/2026", "610", "test", "Toulouse", "35", "40"])