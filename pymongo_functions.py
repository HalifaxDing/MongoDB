from pymongo import MongoClient
import pprint


# CONNECTION_STRING = "mongodb+srv://<username>:<password>@<clustername>.bcdtwrn.mongodb.net/"
CONNECTION_STRING = "mongodb+srv://<username>:<password>@<clustername>.bcdtwrn.mongodb.net/"


def connect_database():
    try:
        # Create a connection using MongoClient.
        client = MongoClient(CONNECTION_STRING)
        return client
    except Exception as e:
        print(f"An error occurred while connecting to the database: {e}")
        return None

def get_database(database_name):
    try:
        client = connect_database()
        if client:
            # Create the database or get information about the database
            return client[database_name]
        else:
            return None
    except Exception as e:
        print(f"An error occurred while getting the database: {e}")
        return None

def drop_database(database_name):
    try:
        client = connect_database()
        if client:
            client.drop_database(database_name)
            client.close()
            print(f"The '{database_name}' database has been dropped.")
        else:
            print("Database connection not established.")
    except Exception as e:
        print(f"An error occurred while dropping the database: {e}")

def list_databases():
    try:
        client = connect_database()
        if client:
            database_list = client.list_database_names()
            client.close()
            print("List of databases:")
            for db in database_list:
                print(db)
        else:
            print("Database connection not established.")
    except Exception as e:
        print(f"An error occurred while listing the databases: {e}")


def highlight_keyword(obj, keyword):
    # Pretty print the object using pprint
    pp = pprint.PrettyPrinter()
    output = pp.pformat(obj)

    # Check if the keyword exists in the output
    if keyword in output:
        # Highlight the keyword by wrapping it with ANSI escape codes for color (here, using red color)
        highlighted_output = output.replace(keyword, f"\033[91m{keyword}\033[0m")
        print(highlighted_output)
    else:
        print(output)  # If keyword not found, print the original output as is


# # This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
  
   # Get the database
   dbname = get_database("Default_DB")
   print(dbname)

