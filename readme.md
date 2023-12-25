# prepare virtual environment

python -m venv venv

3.4 above

## activate
venv\Scripts\activate.bat

venv\Scripts\Activate.ps1

## macOS
source venv/bin/activate

# Install mongoDB
pip install -r requirements.txt

## pymongo install only
python -m pip install "pymongo[srv]"
## panda install only
python -m pip install "panda" 
## panda dateutil only
python -m pip install python-dateutil

# Sign up free tier
https://www.mongodb.com/cloud/atlas/register

# Create cluster
https://www.mongodb.com/docs/atlas/tutorial/create-new-cluster/

# Start python
python

# Exit python
ctrl Z

# MongoDB connection string

mongodb+srv://[username]:[password]@[clustername].bcdtwrn.mongodb.net/

# Reference

https://www.mongodb.com/languages/python

# Airbnb Sample Data

http://insideairbnb.com/get-the-data/


# Exploring database

py_main.py

# Import data from csv file

py_import_csv.py

# Sample query

py_query.py

# MongoDB Atlas documentation

[MongoDB documentation.pdf](https://github.com/HalifaxDing/MongoDB/blob/main/MongoDB%20documentation.pdf)
