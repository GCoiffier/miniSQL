(SELECT e.nom FROM "employes.csv" e) MINUS (SELECT e2.nom FROM "employes.csv" e2, "departements.csv" d WHERE e2.dpt!=d.idd)
