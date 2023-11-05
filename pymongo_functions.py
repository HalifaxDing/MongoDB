from pymongo import MongoClient

def connect_database(connection_string):
    try:
        # Create a connection using MongoClient.
        client = MongoClient(connection_string)
        return client
    except Exception as e:
        print(f"An error occurred while connecting to the database: {e}")
        return None

def get_database(connection_string, database_name):
    try:
        client = connect_database(connection_string)
        if client:
            # Create the database or get information about the database
            return client[database_name]
        else:
            return None
    except Exception as e:
        print(f"An error occurred while getting the database: {e}")
        return None

def drop_database(connection_string, database_name):
    try:
        client = connect_database(connection_string)
        if client:
            client.drop_database(database_name)
            client.close()
            print(f"The '{database_name}' database has been dropped.")
        else:
            print("Database connection not established.")
    except Exception as e:
        print(f"An error occurred while dropping the database: {e}")

def list_databases(connection_string):
    try:
        client = connect_database(connection_string)
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




# # This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
  
   # Get the database
   dbname = get_database("Default_DB")
   print(dbname)

