# Solr commands

## Running solr
- docker run --name f1_solr -p 9000:8983 solr:8.10

## Creating collection/core
- docker exec b9e4fdb6be5d bin/solr create_core -c courses

## Populating collection
- **API**: curl -X POST -H 'Content-type:application/csv' --data-binary @C:\Users\'Diogo Nunes'\'OneDrive - Universidade do Porto'\FEUP\Formula1\processed_data\circuits_text.csv localhost:9000/solr/f1/update?commit=true