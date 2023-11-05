from pymongo_functions import *
from pprint import pprint


# CONNECTION_STRING = "mongodb+srv://<username>:<password>@clustersmu.bcdtwrn.mongodb.net/<clustername>"
CONNECTION_STRING = "mongodb+srv://<username>:<password>@clustersmu.bcdtwrn.mongodb.net/<clustername>"

# list_databases(CONNECTION_STRING)

# Connect Database
dbname = get_database(CONNECTION_STRING, "AirBnb_Data")

# Create Collection
collection = dbname["Reviews"]

# # 1. Sort by id
# results = collection.find().sort('id',1).limit(30)
# for result in results:
#     print(result)


# # 2. Find - Filter
# result = collection.find_one({"name": "Hank"})
# print(result)

# result = collection.find_one({"reviewer_name": "Hank"})
# print(result)

# results = collection.find({"reviewer_name": "Hank"})
# for result in results:
#     print(result)


# # 3. Update a Document
# update_query = {"reviewer_name": "Hank", "date": "2023-08-15"}
# new_values = {"$set": {"date": "2023-08-14"}}
# collection.update_one(update_query, new_values)

# result = collection.find_one({"reviewer_name": "Hank", "date": "2023-08-15"})
# print(result)


# # 4. Delete a Document:
# item = {
#   "reviewer_name" : "Hank",
# "date": "2023-08-15"
# }
# collection.insert_one(item)
# delete_query = {"reviewer_name": "Hank", "date": "2023-08-15"}
# collection.delete_one(delete_query)


# # 5. Query with Filters:
# filtered_results = collection.find({"reviewer_name": {"$regex": "^J"}}).sort('id',1).limit(30)
# for result in filtered_results:
#     # print(result)
#     pprint(result)


# # 6. Count Documents
# document_count = collection.count_documents({})
# document_count = collection.count_documents({"reviewer_name": "Hank"})
# print(f"Total documents in collection: {document_count}")


# # 7. Aggregate Query
# pipeline = [
#     {"$group": {"_id": "$reviewer_name", "count": {"$sum": 1}}},
#     {"$sort": {"count": -1, "reviewer_name": 1}},
#     {"$limit": 100}
# ]
# results = collection.aggregate(pipeline)
# for result in results:
#     print(result)
