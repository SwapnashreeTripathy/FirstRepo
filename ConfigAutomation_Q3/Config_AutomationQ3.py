from flask import jsonify, request, Flask
from pymongo import MongoClient
from pandasCSV import getitems

client = MongoClient('mongodb+srv://swapnashreet95:VOtxVo6jXyaKXboI@devops.mnvxfkr.mongodb.net/')
db = client["MetaData"]
collection = db['Info']

app = Flask(__name__)

@app.route('/dbinfo', methods=['POST'])
def dbinfo_Post():
    items= request.json
    items=collection.insert_one(getitems())
    return jsonify [{"message": "DB infomation added successfully" }]

@app.route('/dbinfo', methods=['GET'])
def dbinfo_Get():
    items=list(collection.find({},{ '_id': 0 }))
    return jsonify (items)


if __name__ == "__main__":
    app.run(port=3000, debug=True)
