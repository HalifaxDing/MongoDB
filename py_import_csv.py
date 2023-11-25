from pymongo_functions import *
import pandas as pd

# CONNECTION_STRING = "mongodb+srv://<username>:<password>@<clustername>.bcdtwrn.mongodb.net/"
CONNECTION_STRING = "mongodb+srv://<username>:<password>@<clustername>.bcdtwrn.mongodb.net/"

# Connect Database
dbname = get_database(CONNECTION_STRING, "AirBnb_Data")


# Import reviews.csv
# Create Collection
collection = dbname["Reviews"]

# Read the CSV file
df = pd.read_csv('reviews.csv')


# # Import listings.csv
# # Create Collection
# collection = dbname["Listings"]

# # Read the CSV file
# df = pd.read_csv('listings.csv')


# # Import calendar.csv - Too big - Exceed Database Size
# # Create Collection
# collection = dbname["Calendar"]

# # Read the CSV file
# df = pd.read_csv('calendar.csv')


# Convert the data to a dictionary to insert into MongoDB
data = df.to_dict(orient='records')

collection.insert_many(data)

print("Data imported successfully into MongoDB.")
