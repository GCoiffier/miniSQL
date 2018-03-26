SELECT e.nom AS emp, d.dpt as dpt
FROM Employes e, Departements d
WHERE e.dpt = d.idd;
