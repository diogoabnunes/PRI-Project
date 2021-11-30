# Solr

## Running Solr
- docker run -p 8983:8983 my_solr
- docker run --name my_solr -p 8983:8983 solr:8.10

## Creating collection/core
- docker exec eb08a48b993d bin/solr create_core -c courses

## Populating collection
- **API**: curl -X POST -H 'Content-type:application/json' --data-binary @C:\Users\'Diogo Nunes'\'OneDrive - Universidade do Porto'\FEUP\Formula1\tutorial_solr\meic_courses.json localhost:8983/solr/courses/update?commit=true

- **post tool**: docker exec eb08a48b993d bin/post -h

## Delete a core
- docker exec 72d1e6d3bdb6 bin/solr delete -c courses

## Schemas and Analyzers
- curl -X POST -H 'Content-type:application/json' --data-binary @C:\Users\'Diogo Nunes'\'OneDrive - Universidade do Porto'\FEUP\Formula1\tutorial_solr\simple_schema.json localhost:8983/solr/courses/schema

## GET's
- curl -X GET http://localhost:8983/solr/courses/schema/fields/title
- curl -X GET http://localhost:8983/solr/courses/schema/fieldtypes/courseTitle