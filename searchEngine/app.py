from flask import Flask
from flask import request
from flask_pymongo import PyMongo
from flask import jsonify
from bson.json_util import dumps

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'searchEngine'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/searchEngine'

mongo = PyMongo(app)


def debug(data):
    print('*' * 1000)
    print(data)
    print('*' * 1000)


# @app.route('/search', methods=['GET'])
# def search():
#     retDocuments = ''
#     data = request.args['title']
#     debug(data)
#     myQuery = {'title': {'$regex': data}}
#     collection = mongo.db.queries
#     for i in collection.find(myQuery):
#         # for i in collection.find({'_id': 0}):
#         retDocuments += '{}-{}'.format(str(i['title']), str(i['content'])) + '|'
#     return str(retDocuments)

@app.route('/search', methods=['GET'])
def search():
    data = request.args["title"]
    myQuery = {'title': {'$regex': data}}
    collection = mongo.db.queries
    retDocuments = [i for i in collection.find(myQuery, {'_id': 0})]
    return jsonify(retDocuments)


@app.route('/insert', methods=['POST'])
def insert():
    title = request.json['title']
    content = request.json['content']
    collection = mongo.db.queries
    collection.insert({'title': title, 'content': content})
    return 'OK'


if __name__ == '__main__':
    app.run(debug=True)
