from pymongo import MongoClient
from pprint import pprint


# Provide the mongodb Atlas url to connect python to mongodb using pymongo
# cryptouser --> read-only user
CONNECTION_STRING = "mongodb+srv://cryptouser:Uq1RfeOhsY2MAJCF@cryptodb.jsd2tzz.mongodb.net/?retryWrites=true&w=majority"

# admin --> read and write user
CONNECTION_STRING = "mongodb+srv://admin:0Z7397SpvtBeq1gZ@cryptodb.jsd2tzz.mongodb.net/?retryWrites=true&w=majority"



class DB:
    def __init__(self):
        self.client = MongoClient(CONNECTION_STRING, tls=True, tlsAllowInvalidCertificates=True)

    def _add_db(self, name):
        self.db = self.client[name]

    def _add_collection(self, name):
        self.collection = self.db[name]

    def _add_post(self, post: dict):
        self.post = self.collection.insert_one(post).inserted_id

    def find_one(self, prompt):
        self.query = self.collection.find_one(prompt)
