(SELECT * FROM "employes.csv" e WHERE e.ide>3) MINUS (SELECT * FROM "employes.csv" e WHERE e.ide>6);
