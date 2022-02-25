<<<<<<< HEAD
docker exec 1eec8daa181d bin/solr delete -c races_default
docker exec 1eec8daa181d bin/solr delete -c races_schema

docker exec 1eec8daa181d bin/solr create_core -c races_default
docker exec 1eec8daa181d bin/solr create_core -c races_schema
=======
docker exec 8d4b10ab44f1 bin/solr delete -c races_default
docker exec 8d4b10ab44f1 bin/solr delete -c races_schema
docker exec 8d4b10ab44f1 bin/solr delete -c races_boost

docker exec 8d4b10ab44f1 bin/solr create_core -c races_default
docker exec 8d4b10ab44f1 bin/solr create_core -c races_schema
docker exec 8d4b10ab44f1 bin/solr create_core -c races_boost
>>>>>>> 9d9befc38c6eaf646178f3b24ea03e1e6a754635

# Default (without schema)
curl -X POST -H 'Content-type:application/json' --data-binary @./data/schema/configDefault.json http://localhost:8983/solr/races_default/config

curl -X POST -H 'Content-type:application/json' --data-binary @./data/final_json/races.json localhost:8983/solr/races_default/update?commit=true
curl -X POST -H 'Content-type:application/json' --data-binary @./data/final_json/seasons.json localhost:8983/solr/races_default/update?commit=true
curl -X POST -H 'Content-type:application/json' --data-binary @./data/final_json/drivers.json localhost:8983/solr/races_default/update?commit=true
curl -X POST -H 'Content-type:application/json' --data-binary @./data/final_json/constructors.json localhost:8983/solr/races_default/update?commit=true
curl -X POST -H 'Content-type:application/json' --data-binary @./data/final_json/circuits.json localhost:8983/solr/races_default/update?commit=true
curl -X POST -H 'Content-type:application/json' --data-binary @./data/final_json/pages.json localhost:8983/solr/races_default/update?commit=true

# Schema
curl -X POST -H 'Content-type:application/json' -d @./data/schema/schema.json http://localhost:8983/solr/races_schema/schema
curl -X POST -H 'Content-type:application/json' --data-binary @./data/schema/configSchema.json http://localhost:8983/solr/races_schema/config

curl -X POST -H 'Content-type:application/json' --data-binary @./data/final_json/races.json localhost:8983/solr/races_schema/update?commit=true
curl -X POST -H 'Content-type:application/json' --data-binary @./data/final_json/seasons.json localhost:8983/solr/races_schema/update?commit=true
curl -X POST -H 'Content-type:application/json' --data-binary @./data/final_json/drivers.json localhost:8983/solr/races_schema/update?commit=true
curl -X POST -H 'Content-type:application/json' --data-binary @./data/final_json/constructors.json localhost:8983/solr/races_schema/update?commit=true
curl -X POST -H 'Content-type:application/json' --data-binary @./data/final_json/circuits.json localhost:8983/solr/races_schema/update?commit=true
curl -X POST -H 'Content-type:application/json' --data-binary @./data/final_json/pages.json localhost:8983/solr/races_schema/update?commit=true

# Schema with boosts
curl -X POST -H 'Content-type:application/json' -d @./data/schema/schema.json http://localhost:8983/solr/races_boost/schema
curl -X POST -H 'Content-type:application/json' --data-binary @./data/schema/configBoost.json http://localhost:8983/solr/races_boost/config

curl -X POST -H 'Content-type:application/json' --data-binary @./data/final_json/races.json localhost:8983/solr/races_boost/update?commit=true
curl -X POST -H 'Content-type:application/json' --data-binary @./data/final_json/seasons.json localhost:8983/solr/races_boost/update?commit=true
curl -X POST -H 'Content-type:application/json' --data-binary @./data/final_json/drivers.json localhost:8983/solr/races_boost/update?commit=true
curl -X POST -H 'Content-type:application/json' --data-binary @./data/final_json/constructors.json localhost:8983/solr/races_boost/update?commit=true
curl -X POST -H 'Content-type:application/json' --data-binary @./data/final_json/circuits.json localhost:8983/solr/races_boost/update?commit=true
curl -X POST -H 'Content-type:application/json' --data-binary @./data/final_json/pages.json localhost:8983/solr/races_boost/update?commit=true