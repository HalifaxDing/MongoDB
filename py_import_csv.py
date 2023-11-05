from pymongo_functions import *
import pandas as pd

# CONNECTION_STRING = "mongodb+srv://<username>:<password>@clustersmu.bcdtwrn.mongodb.net/<clustername>"
CONNECTION_STRING = "mongodb+srv://<username>:<password>@clustersmu.bcdtwrn.mongodb.net/<clustername>"

# Connect Database
dbname = get_database(CONNECTION_STRING, "AirBnb_Data")


# Create Collection
collection = dbname["Reviews"]
# collection = dbname["Listings"]

# Read the CSV file
df = pd.read_csv('reviews.csv')
# df = pd.read_csv('listings.csv')


# Convert the data to a dictionary to insert into MongoDB
data = df.to_dict(orient='records')

collection.insert_many(data)

print("Data imported successfully into MongoDB.")
