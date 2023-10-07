from modules.mongodb import MongoDB


def backup(dbName):

    try:

        mongo = MongoDB(dbName)
        collections = mongo.getCollections()

        if (not collections):
            return False

        currentCache = {}

        for collection in collections:
            mongo.collection = collection
            currentCache[collection] = mongo.findMany({})

        mongo.setDatabase(dbName + '-backup')

        for collection in collections:
            mongo.collection = collection

            insertedIds = mongo.insertMany(currentCache[collection])
            mongo.deleteMany({'_id': {'$nin': insertedIds}})

    except Exception:
        raise (Exception)
