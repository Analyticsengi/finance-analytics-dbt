 # Creation CSV Sale
 ## Contexte
Le but est de generer unn CSV financier volontairement sale pour s'entrainer au SQL. On utilisera python pour le faire.
On part de l'hypothèse que l'année par défault est 2026.
J'y ajoute les défault volontaires : l'absence de centre de coûts, le libellé incohérent, les années hors exercies

## Le fichier produit

Produit 500 lignes(hors titre) CSV, avec séparateur via point-virgule.
Cela génère 6 colonnes : Date;Numéro de compte;Libellé;Centre de coût;Mouvement;Montant


## Défauts volontaires

### 1. Absence du centre de coût

A partir de 7eme mois toutes les champs Centre B disparaissent


### 2. Libellés incohérent

Volontairement remplacer certains libellé par "salaires" qui hors de propors dans mon tableau.

### 3. Années hors exercice


remplacer l'année par default 2026 par 2024 ou 2025 avec parfois des lien d'erreur avec l'incohérence 2.



## Prochaine étape

[Chargement dans DuckDB et nettoyage en SQL]