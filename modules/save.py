from modules.mongodb import MongoDB


def save(dbName, collectionName, data):

    try:
        mongo = MongoDB(dbName)
        mongo.collection = collectionName

        insertedIds = mongo.insertMany(data)
        mongo.deleteMany({'_id': {'$nin': insertedIds}})

    except Exception:
        raise Exception
