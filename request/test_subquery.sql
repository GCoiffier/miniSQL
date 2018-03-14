SELECT dep.nom FROM (SELECT dep2.id,dep2.nom FROM "departements.csv" dep2) dep1;
