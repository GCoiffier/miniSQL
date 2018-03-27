SELECT e.key, e.name
FROM "test3.csv" e
WHERE e.name NOT IN ( SELECT f.name
                      FROM "test3.csv" f, "test3.csv" g
                      WHERE f.age > e.age
                        AND f.score > g.score
                        AND g.age = e.age)
