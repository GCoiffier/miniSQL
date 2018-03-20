SELECT e.dpt, e.nom
FROM "employes.csv" e
WHERE e.dpt IN ( SELECT e.dpt
                 FROM "employes.csv" e, "departements.csv" ds
                 WHERE ds.directeur = e.ide
                    AND ds.idd IN ( SELECT v.dpt
                                    FROM "employes.csv" v
                                    WHERE e.dpt = ds.idd));