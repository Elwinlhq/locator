# -- INSTALL MIGRATION TOOL 

sudo npm install db-migrate
sudo npm install mysql


# -- Set up the config at database.json
{
  "test": {
    "driver": "mysql",
    "user": "[you user]",
    "password": "[your pass]",
    "host": "localhost",
    "database": "liquitest"
  },
}

# -- Create the basic schema
cat drop.sql create.sql insert.sql test_data.sql | mysql -u[you user] -p[your pass] liquitest 

node_modules/db-migrate/bin/db-migrate --env test --migrations-dir=./migrations create add_category_to_project
node_modules/db-migrate/bin/db-migrate --env test --migrations-dir=./migrations up add_category_to_project -v
node_modules/db-migrate/bin/db-migrate --env test --migrations-dir=./migrations down  

node_modules/db-migrate/bin/db-migrate --env test --migrations-dir=./migrations create update_category_field
node_modules/db-migrate/bin/db-migrate --env test --migrations-dir=./migrations up update_category_field -v
node_modules/db-migrate/bin/db-migrate --env test --migrations-dir=./migrations down  

node_modules/db-migrate/bin/db-migrate --env test --migrations-dir=./migrations create drop_category_foreign_key
node_modules/db-migrate/bin/db-migrate --env test --migrations-dir=./migrations up drop_category_foreign_key -v
# No downgrade migration is provided
# node_modules/db-migrate/bin/db-migrate --env test --migrations-dir=./migrations down  

node_modules/db-migrate/bin/db-migrate --env test --migrations-dir=./migrations create rebuild_view
node_modules/db-migrate/bin/db-migrate --env test --migrations-dir=./migrations up rebuild_view -v
# No downgrade migration is provided
# node_modules/db-migrate/bin/db-migrate --env test --migrations-dir=./migrations down 

