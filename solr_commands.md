# Solr commands

## Running solr
- docker desktop

## Creating collection/core
- docker exec 050b84d33977 bin/solr create_core -c races
- docker exec 050b84d33977 bin/solr create_core -c default

## Populating collection
- **API**: curl -X POST -H 'Content-type:application/csv' --data-binary @C:\Users\'Diogo Nunes'\'OneDrive - Universidade do Porto'\FEUP\PRI\Formula1\documentos_resultado\races_joined.csv localhost:8983/solr/races/update?commit=true
- curl -X POST -H 'Content-type:application/csv' --data-binary @C:\Users\'Diogo Nunes'\'OneDrive - Universidade do Porto'\FEUP\PRI\Formula1\documentos_resultado\races_joined.csv localhost:8983/solr/default/update?commit=true

## Schema
- **API**: curl -X POST -H 'Content-type:application/json' -d @C:\Users\'Diogo Nunes'\'OneDrive - Universidade do Porto'\FEUP\PRI\Formula1\schema\schema.json http://localhost:8983/solr/races/schema

## Deleting collection/core
- docker exec 050b84d33977 bin/solr delete -c races
- docker exec 050b84d33977 bin/solr delete -c default