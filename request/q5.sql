SELECT p.titre, COUNT(m.idp)
FROM "projets.csv" p, "membres.csv" m
WHERE m.idp=p.idp
GROUP BY p.titre;
