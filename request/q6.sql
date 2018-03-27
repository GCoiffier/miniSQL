(SELECT s.dpt
 FROM "employes.csv" s, "departements.csv" ds
 WHERE ds.directeur = s.ide)

UNION

(SELECT s.dpt
 FROM "employes.csv" e, "employes.csv" s, "departements.csv" ds
 WHERE e.dpt = ds.idd);
