from os import name
from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'contact': u'-74327309835',
        'name': u'Raj',
        'done': False
    },
    {
        'id': 2,
        'contact': u'54370979057905',
        'name': u'Mohan',
        'done': False
    }
]

@app.route("/")
def Hello_world():
    return 'Hello World'

@app.route("/get-data")
def get_task():
    return jsonify({"data":tasks})

@app.route("/add-data", methods=["POST"])
def add_task():
    if(not request.json):
        return jsonify({"Status": "Error", "Message": "Please provide the data"}, 400)
    task = {
        'id': tasks[-1]['id']+1,
        'contact': request.json['contact'],
        'name': request.json.get('name', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({"Status": "Successfull", "Message": "Task is updated sir/madam."})

if __name__ =="__main__":
    app.debug = True
    app.run()