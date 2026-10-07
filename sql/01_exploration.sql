--Compter les lignes ou le centre est Null


SELECT MONTH("Date") as "Mois","Centre de coût",COUNT("Centre de Coût") as Nb
FROM read_csv('ma_compta_sales.csv',dateformat='%d/%m/%Y')
WHERE "Centre de coût"= 'Centre B'
GROUP BY MONTH("date") ,"Centre de coût"
ORDER BY MONTH("date") ASC;