--Trouver les année différent de 2026
--Prédiction: ~ 25  | Realisé: 26

SELECT COUNT(*) as "Nb"
FROM read_csv('ma_compta_sales.csv',dateformat='%d/%m/%Y')
WHERE YEAR("Date") <>2026;