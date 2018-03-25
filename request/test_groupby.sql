SELECT e.nom, e.dpt, MAX(e.ide) FROM "employes.csv" e GROUP BY e.dpt;
