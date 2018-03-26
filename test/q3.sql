SELECT DISTINCT p.titre, e.nom
FROM Employes e, Projets p, Membres m
WHERE e.ide = m.ide
  AND m.idp = p.idp
  AND e.dpt NOT IN (SELECT r.dpt
                    FROM Employes r
                    WHERE r.ide = p.responsable)
ORDER BY p.titre, e.nom
;
