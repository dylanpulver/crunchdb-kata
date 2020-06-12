# Steps For Running The Application Locally

## Create pipenv and install packages
pipenv shell
pipenv install pymongo

## Start mongodb in terminal (done on mac, useful resource I utilized: https://zellwk.com/blog/install-mongodb/ and https://zellwk.com/blog/local-mongodb/)
brew services run mongodb-community
brew services list
mongo
use preferences_db

# Testing Notes
## mongodb shell testing commands used
check current database: db
create a newly named database: use preferences_db
list all records in collection (used to test if acquisition script sent data to collection): db.surv_results.find()
count of mongodb collection: db.surv_results.count()
remove all records in mongoDB collection: db.surv_results.remove({})
