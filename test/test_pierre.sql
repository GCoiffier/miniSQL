SELECT e.dpt, e.nom
FROM Employes e
WHERE e.dpt IN ( SELECT e.dpt
                 FROM Employes e, Departements ds
                 WHERE ds.directeur = e.ide
                    AND ds.idd IN ( SELECT v.dpt
                                    FROM Employes v
                                    WHERE e.dpt = ds.idd));
