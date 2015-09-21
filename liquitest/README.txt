# SAMPLE USAGE FOR LIQUIBASE WITH EXISTING SCHEMA

# -- Simulate the schema and get reverse engineering the migrations

# Dummy make all
cat drop.sql create.sql insert.sql test_data.sql | mysql -u<your user> -p<your pass> liquitest 

# Reverse engineering basic schema
cat drop.sql create.sql | mysql -u<your user> -p<your pass> liquitest 
liquibase --changeLogFile="./boot.xml" generateChangeLog

# Reverse engineering categories table
cat drop.sql create.sql insert.sql | mysql -u<your user> -p<your pass> liquitest 
liquibase --changeLogFile="./init_categories.xml" --diffTypes="data" generateChangeLog

# Reverse engineering sample data (Delete by hand the categories insert)
cat drop.sql create.sql insert.sql test_data.sql | mysql -u<your user> -p<your pass> liquitest 
liquibase --changeLogFile="./init_sample_data.xml" --diffTypes="data" generateChangeLog



# -- Create and update the metadata of the migration engine
liquibase --changeLogFile=./boot.xml changeLogSync
liquibase --changeLogFile=./init_categories.xml changeLogSync
liquibase --changeLogFile=./init_sample_data.xml changeLogSync





# -- New schema, simulate all migrations
cat drop.sql | mysql -u<your user> -p<your pass> liquitest 
liquibase --changeLogFile=./boot.xml migrate
liquibase --changeLogFile=./init_categories.xml migrate
liquibase --changeLogFile=./init_sample_data.xml migrate
liquibase --changeLogFile=./artist.xml migrate
