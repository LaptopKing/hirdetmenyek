from pymongo import MongoClient
from bson.objectid import ObjectId


class MongoDB():
    def __init__(self, dbName):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client[dbName]
        self.collection = ''

    def setDatabase(self, dbName):

        try:
            self.db = self.client[dbName]
        except Exception:
            self.errorHandler(Exception)

    def getCollections(self):

        try:
            return self.db.list_collection_names()
        except Exception:
            self.errorHandler(Exception)

    def insertOne(self, data):

        try:
            return self.db[self.collection].insert_one(data).inserted_id
        except Exception:
            self.errorHandler(Exception)

    def insertMany(self, data):

        try:
            return self.db[self.collection].insert_many(data).inserted_ids
        except Exception:
            self.errorHandler(Exception)

    def findOneByObjectId(self, _id):

        try:
            return self.db[self.collection].find_one({'_id': ObjectId(_id)})
        except Exception:
            self.errorHandler(Exception)

    def findOne(self, data):

        try:
            return self.db[self.collection].find_one(data)
        except Exception:
            self.errorHandler(Exception)

    def findMany(self, data):

        try:
            return self.db[self.collection].find(data)
        except Exception:
            self.errorHandler(Exception)

    def deleteMany(self, data):

        try:
            return self.db[self.collection].delete_many(data)
        except Exception:
            self.errorHandler(Exception)

    def errorHandler(self, error):
        raise (error)
