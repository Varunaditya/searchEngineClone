from flask import Flask, request, jsonify, make_response
from dbSetup import createConnection, createCollection, insertDocument, getDocument

app = Flask(__name__)

db = createConnection('searchEngine')

collection = createCollection(db, 'queries')


def main():
    global db, collection


@app.route('/search', methods=['GET'])
def search():
    data = request.args.get('string')
    myQuery = {'title': {'$regex': data}}
    return getDocument(collection, myQuery)


@app.route('/insert', methods = ['POST'])
def insert():
    title = request.args.get('title')
    content = request.args.get('content')
    insertDocument(collection, title, content)
    return


if __name__ == '__main__':
    main()
    app.run(debug=True)


