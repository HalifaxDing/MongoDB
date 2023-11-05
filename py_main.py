from pymongo_functions import *


# CONNECTION_STRING = "mongodb+srv://<username>:<password>@clustersmu.bcdtwrn.mongodb.net/<clustername>"
CONNECTION_STRING = "mongodb+srv://<username>:<password>@clustersmu.bcdtwrn.mongodb.net/<clustername>"

# list_databases(CONNECTION_STRING)

# Connect Database
dbname = get_database(CONNECTION_STRING, "AirBnb_Data")

# Create Collection
collection = dbname["Reviews"]


# Connect Database
# dbname = get_database(CONNECTION_STRING, "Default_DB")

# Drop Database
# drop_database(CONNECTION_STRING, "Default_DB")

# Create a new collection
# collection_name = dbname["Test_Collection"]

# expiry_date = '2021-07-13T00:00:00.000Z'
# expiry = parser.parse(expiry_date)
# item_1 = {
#   "item_name" : "Bread",
#   "quantity" : 2,
#   "ingredients" : "all-purpose flour",
#   "expiry_date" : expiry
# }
# collection_name.insert_one(item_1)

# for coll in dbname.list_collection_names():
#     print(coll)

# print(dbname)