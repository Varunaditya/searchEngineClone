import pymongo


def createConnection(database):
    dbClient = pymongo.MongoClient('mongodb://localhost:27017/')
    return dbClient[database]


def createCollection(db, collectionName):
    return db[collectionName]


def insertDocument(collection, title, content):
    payLoad = {
                'title': title,
                'content': content
              }
    collection.insert_one(payLoad)


def main():
    db = createConnection('searchEngine')
    collection = createConnection(db, 'queries')
    print('OK')


if __name__ == '__main__':
    main()
