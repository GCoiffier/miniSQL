SELECT e.dpt, e.nom
FROM "employes.csv" e
WHERE e.dpt IN ( SELECT f.dpt
                 FROM "employes.csv" f, "departements.csv" ds
                 WHERE ds.directeur = f.ide
                    AND ds.idd IN ( SELECT v.dpt
                                    FROM "employes.csv" v
                                    WHERE f.dpt = ds.idd));
