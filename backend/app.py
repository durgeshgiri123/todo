from flask import Flask, request
from dotenv import load_dotenv
import os
import pymongo
load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')
client = pymongo.MongoClient(MONGO_URI)
db = client.test
Collection = db['PYTHON']
app = Flask(__name__)
@app.route('/submit', methods=['POST'])
def submit():
    form_data = dict(request.json)
    Collection.insert_one(form_data)
    return 'To do item Data submitted successfully'
@app.route('/view')
def view ():
    data = Collection.find()
    data_list = list(data)
    for item in data:
        print(item)
        del item['_id']
    data = {
        'data': data
    }
    return data
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)