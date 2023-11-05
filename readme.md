# prepare virtual environment

python -m venv venv

3.4 above

## activate
venv\Scripts\activate.bat
venv\Scripts\Activate.ps1

## macOS
source myvenv/bin/activate

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

# Create cluster.0
https://www.mongodb.com/docs/atlas/tutorial/create-new-cluster/



# Start python
python

# Exit python
ctrl Z

mongodb+srv://<username>:<password>@clustersmu.bcdtwrn.mongodb.net/?retryWrites=true&w=majority



https://www.mongodb.com/languages/python