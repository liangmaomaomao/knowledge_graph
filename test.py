from neo4j import GraphDatabase

# URI examples: "neo4j://localhost", "neo4j+s://xxx.databases.neo4j.io"
URI = "neo4j+s://10dc473a.databases.neo4j.io"
AUTH = ("neo4j", "dsHH9XN67B-LaV4odga6qikwDgJ9DX3nRw9JN56hz_U")

with GraphDatabase.driver(URI, auth=AUTH) as driver:
    driver.verify_connectivity()
