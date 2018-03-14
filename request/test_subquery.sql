SELECT dep.nom FROM (SELECT dep2.idd,dep2.nom FROM "departements.csv" dep2) dep;
