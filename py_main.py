from pymongo_functions import *
from dateutil import parser


# CONNECTION_STRING = "mongodb+srv://<username>:<password>@<clustername>.bcdtwrn.mongodb.net/"
CONNECTION_STRING = "mongodb+srv://<username>:<password>@<clustername>.bcdtwrn.mongodb.net/"


# # 1. List Databases
# list_databases(CONNECTION_STRING)


# # 2. Connect Database
# dbname = get_database(CONNECTION_STRING, "Default_DB")
# print(dbname)

# Create a new collection
# collection_name = dbname["Test_Collection"]


# # 3. List collection
# print()
# print("List of collection:")
# for coll in dbname.list_collection_names():
#     print(coll)


# # 4. Insert Data
# expiry_date = '2021-07-13T00:00:00.000Z'
# expiry = parser.parse(expiry_date)
# item_1 = {
#   "item_name" : "Bread",
#   "quantity" : 2,
#   "ingredients" : "all-purpose flour",
#   "expiry_date" : expiry
# }
# collection_name.insert_one(item_1)


# # 5. Drop Database
# drop_database(CONNECTION_STRING, "Default_DB")

# # Verify
# list_databases(CONNECTION_STRING)
