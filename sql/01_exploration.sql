--Trouver les année différent de 2026 et les ligne salaires en même temps
-- avec OR 34 et AND ( la bonne réponse) 15
SELECT COUNT(*) as "Nb",COUNT("Centre de coût") as "nb non vide",("Nb" - "nb non vide") as "Total"
FROM read_csv('ma_compta_sales.csv',dateformat='%d/%m/%Y');