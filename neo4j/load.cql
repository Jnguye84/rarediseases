LOAD CSV WITH HEADERS FROM 'file:///output.csv' AS row
WITH row WHERE row.Contributors IS NOT NULL
MERGE (v:Variant {name: row.`Allelic variant list`})
MERGE (r:Reference {citation: row.`Reference list`})
MERGE (l:Link {url: row.`External links`})
MERGE (c:Contributor {name: row.Contributors})
MERGE (v)-[:HAS_REFERENCE]->(r)
MERGE (r)-[:HAS_LINK]->(l)
MERGE (v)-[:CONTRIBUTED_BY]->(c);
