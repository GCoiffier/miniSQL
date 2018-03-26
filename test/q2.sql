SELECT e.dpt, e.nom
FROM Employes e
WHERE e.dpt IN ( SELECT s.dpt
                 FROM Employes s, Departements ds
                 WHERE ds.directeur = s.ide
                   AND e.dpt = ds.idd);
