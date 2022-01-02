docker exec 050b84d33977 bin/solr delete -c races_default
docker exec 050b84d33977 bin/solr delete -c races_schema
docker exec 050b84d33977 bin/solr delete -c races_boost

docker exec 050b84d33977 bin/solr create_core -c races_default
docker exec 050b84d33977 bin/solr create_core -c races_schema
docker exec 050b84d33977 bin/solr create_core -c races_boost

# Default (without schema)
curl -X POST -H 'Content-type:application/csv' --data-binary @C:\\Users\\'Diogo Nunes'\\'OneDrive - Universidade do Porto'\\FEUP\\PRI\\Formula1\\documentos_resultado\\races_joined.csv localhost:8983/solr/races_default/update?commit=true

# Schema
curl -X POST -H 'Content-type:application/json' -d @C:\\Users\\'Diogo Nunes'\\'OneDrive - Universidade do Porto'\\FEUP\\PRI\\Formula1\\schema\\schema.json http://localhost:8983/solr/races_schema/schema
curl -X POST -H 'Content-type:application/csv' --data-binary @C:\\Users\\'Diogo Nunes'\\'OneDrive - Universidade do Porto'\\FEUP\\PRI\\Formula1\\documentos_resultado\\races_joined.csv localhost:8983/solr/races_schema/update?commit=true
curl -X POST -H 'Content-type:application/csv' --data-binary @C:\\Users\\'Diogo Nunes'\\'OneDrive - Universidade do Porto'\\FEUP\\PRI\\Formula1\\documentos_resultado\\seasons_joined.csv localhost:8983/solr/races_schema/update?commit=true
curl -X POST -H 'Content-type:application/csv' --data-binary @C:\\Users\\'Diogo Nunes'\\'OneDrive - Universidade do Porto'\\FEUP\\PRI\\Formula1\\documentos_resultado\\drivers_joined.csv localhost:8983/solr/races_schema/update?commit=true
curl -X POST -H 'Content-type:application/csv' --data-binary @C:\\Users\\'Diogo Nunes'\\'OneDrive - Universidade do Porto'\\FEUP\\PRI\\Formula1\\documentos_resultado\\constructors_joined.csv localhost:8983/solr/races_schema/update?commit=true
curl -X POST -H 'Content-type:application/csv' --data-binary @C:\\Users\\'Diogo Nunes'\\'OneDrive - Universidade do Porto'\\FEUP\\PRI\\Formula1\\documentos_resultado\\circuits_joined.csv localhost:8983/solr/races_schema/update?commit=true

# Schema with boosts
curl -X POST -H 'Content-type:application/json' -d @C:\\Users\\'Diogo Nunes'\\'OneDrive - Universidade do Porto'\\FEUP\\PRI\\Formula1\\schema\\schema.json http://localhost:8983/solr/races_boost/schema
curl -X POST -H 'Content-type:application/csv' --data-binary @C:\\Users\\'Diogo Nunes'\\'OneDrive - Universidade do Porto'\\FEUP\\PRI\\Formula1\\documentos_resultado\\races_joined.csv localhost:8983/solr/races_boost/update?commit=true