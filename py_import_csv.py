from pymongo_functions import *
import pandas as pd


# Connect Database
dbname = get_database("AirBnb_Data")


# 1. Import Collection - Listings
# Import listings.csv
# Create Collection
collection = dbname["Listings"]

# Read the CSV file
df = pd.read_csv('listings.csv')



# # 2. Import Collection - Reviews
# # Import reviews.csv
# # Create Collection
# collection = dbname["Reviews"]

# # Read the CSV file
# df = pd.read_csv('reviews.csv')



# # 3. Import Collection - Calendar
# # Import calendar.csv - Too big - Exceed Database Size
# # Create Collection
# collection = dbname["Calendar"]

# # Read the CSV file
# df = pd.read_csv('calendar.csv')



# Convert the data to a dictionary to insert into MongoDB
data = df.to_dict(orient='records')

print("Start importing.")

collection.insert_many(data)

print("Data imported successfully into MongoDB.")
