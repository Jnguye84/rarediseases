# Neo4J ADCY5
This directory in the repository explains how to setup and create the Neo4J database.

## Quickstart

1. Run the command `python main.py` to create the JSON file which performs data collection accross the internet.
2. Run the command `python ParseJson.py` creates the CSV.
3. Open the `load.cql` file to create the query from the `output.csv` to run on the cloud Neo4J.

## Cloud Storage
The data is located on https://console.neo4j.io/ and you can find the authentication, urls, and secrets in `keys.txt`.

## Install
- Run `./install.sh`
- Run the command `./neo4j-community-5.17.0/bin/neo4j status` to see the status of the Neo4J database.

## Visualize

Run this query to produce a visualization.

```cypher
MATCH (v:Variant)-[:CONTRIBUTED_BY]->(c:Contributor)
RETURN v, c
```