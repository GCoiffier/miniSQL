SELECT e.nom, MAX(e.ide) FROM "employes.csv" e GROUP BY e.dpt;
