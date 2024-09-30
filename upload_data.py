from pymongo.mongo_client import MongoClient
import pandas as pd # type: ignore
import json

#url
uri="mongodb+srv://abhijitmaharana2580:JHC5cca5O0YfhQws@cluster0.u5xf1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

#create a new client and connectt to server
client = MongoClient(uri)

#create database name and collection name
DATABASE_NAME="'ABHIJIT_MAHARANA'"
COLLECTION_NAME='waferfault'

df=pd.read_csv("C:\Users\91965\OneDrive\Desktop\sensor fault detection\notebooks\wafer_23012020_041211.csv")
df=df.drop("Unnamed: 0",axis=1)

json_record=list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)