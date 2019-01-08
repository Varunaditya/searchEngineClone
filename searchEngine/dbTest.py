import pymongo

dbClient = pymongo.MongoClient("mongodb://localhost:27017/")

db = dbClient['testDB#1']

testCollection = db['testCollection']

payLoad = [
            {
                'name': 'Tamanna',
                '_id': 930
            },
            {
                'name': 'Varunaditya',
                '_id': 113
            }
          ]

# testCollection.insert_many(payLoad)

# for document in testCollection.find():
#     print(document)


#query

myQuery = {'name': {'$regex': ''}}

# for document in testCollection.find(myQuery, {'_id': 0}).sort('name', -1).limit(3):
# for document in testCollection.find(myQuery, {'_id': 0}).sort('name', -1):
#     print(document)

documentToBeDeleted = {'name': {'$regex': 'na$'}}

testCollection.delete_one(documentToBeDeleted)

for document in testCollection.find({}, {'_id': 0}):
    print(document)

#delete collection
# testCollection.drop()

#update document

nameToBeUpdated = 'Varunaditya'

documentToBeUpdated = {'name': nameToBeUpdated}
newValues = {'$set': {'name': nameToBeUpdated + ' Jadwal'}}

testCollection.update_one(documentToBeUpdated, newValues)

for document in testCollection.find({}, {'_id': 0}):
    print(document)
