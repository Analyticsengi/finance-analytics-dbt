--Compter les lignes ou le centre est Null
--Prédiction: ~50 | Obeservé : 54

SELECT MONTH("Date") as "Mois","Centre de coût",COUNT("date") as Nb
FROM read_csv('ma_compta_sales.csv',dateformat='%d/%m/%Y')
WHERE "Centre de coût" IS Null
GROUP BY MONTH("date") ,"Centre de coût"
ORDER BY MONTH("date") ASC;