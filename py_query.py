from pymongo_functions import *


# CONNECTION_STRING = "mongodb+srv://<username>:<password>@<clustername>.bcdtwrn.mongodb.net/"
CONNECTION_STRING = "mongodb+srv://<username>:<password>@<clustername>.bcdtwrn.mongodb.net/"

# list_databases(CONNECTION_STRING)

# Connect Database
dbname = get_database(CONNECTION_STRING, "AirBnb_Data")

# Create Collection
# Default collection selected.
collection = dbname["Reviews"] 
# collection = dbname["Listings"]



# # 1. Sort by id
# # Use collection "Reviews"
# results = collection.find().sort('id',1).limit(30)
# for result in results:
#     print(result)



# # 2. Find - Filter
# # Use collection "Reviews", find reviewer named Hank
# # Expected result: None
# result = collection.find_one({"name": "Hank"})
# print(result)


# # Use collection "Reviews", find reviewer named Hank
# # Expected result: One
# result = collection.find_one({"reviewer_name": "Hank"})
# print(result)
# # pprint(result)


# # Use collection "Reviews", find reviewer named Hank
# # Expected result: Eleven
# results = collection.find({"reviewer_name": "Hank"})
# for result in results:
#     pprint(result)



# # 3. Update a Document
# # Use collection "Reviews"
# update_query = {"reviewer_name": "Hank", "date": "2023-08-15"}
# new_values = {"$set": {"date": "2023-08-14"}}
# collection.update_one(update_query, new_values)

# result = collection.find_one({"reviewer_name": "Hank", "date": "2023-08-15"})
# pprint(result)



# # 4. Delete a Document:
# # Use collection "Reviews"
# item = {
#   "reviewer_name" : "Hank",
# "date": "2023-08-15"
# }
# collection.insert_one(item)
# delete_query = {"reviewer_name": "Hank", "date": "2023-08-15"}
# collection.delete_one(delete_query)



# # 5. Query with Filters:
# # Use collection "Reviews"
# filtered_results = collection.find({"reviewer_name": {"$regex": "^J"}}).sort('id',1).limit(30)
# for result in filtered_results:
#     pprint(result)



# # 6. Count Documents
# # Use collection "Reviews"
# document_count = collection.count_documents({})
# # document_count = collection.count_documents({"reviewer_name": "Hank"})
# print(f"Total documents in collection: {document_count}")



# # 7. Aggregate Query
# # Use collection "Reviews"
# pipeline = [
#     {"$group": {"_id": "$reviewer_name", "count": {"$sum": 1}}},
#     {"$sort": {"count": -1, "reviewer_name": 1}},
#     {"$limit": 100}
# ]
# results = collection.aggregate(pipeline)
# for result in results:
#     print(result)



# # 8. Query with Filters:
# # Use collection "Listings"
# # Expected result: Three
# filtered_results = collection.find({"description": {"$regex": ".*Château.*"}}).sort('id',1).limit(30)
# for result in filtered_results:
#     highlight_keyword(result, "Château")



# # 9. Wide-ranging Search
# # Use collection "Listings", find keyword - Chateau
# # Expected result: Thirteen
# collection.create_index([("$**", "text")]) 
# keyword = "Chateau"
# search_results = collection.find({"$text": {"$search": keyword}})
# for result in search_results:
#     highlight_keyword(result, "Chateau")
#     # highlight_keyword(result, "Château")
#     print()

# # List all indexes
# indexes = collection.list_indexes()
# for index in indexes:
#     print(index)

# # Drop index for text search
# index_name = "$**_text"
# if index_name in collection.index_information():
#     collection.drop_index(index_name)
#     print(f"Index {index_name} droped")
