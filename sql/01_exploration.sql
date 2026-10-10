--Trouver les lignes "Salariés"
--Prédiction: ~ 20  | Realisé: 23

SELECT COUNT(*) as "Nb"
FROM read_csv('ma_compta_sales.csv',dateformat='%d/%m/%Y')
WHERE "Libellé"='salaires';