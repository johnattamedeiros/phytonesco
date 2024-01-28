from flask import Flask
from flask import jsonify
from flask import request
import json
from flask_cors import CORS #include this line

#read file
with open('tasks.json','r') as myfile:
    data=myfile.read()
#parse file
tasksData = json.loads(data)

app = Flask(__name__)
app.run(debug=True)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/todo/get',methods=['GET'])
def getTasks():
    return jsonify(tasksData)

@app.route('/todo/create',methods=['POST'])
def createTask():
    req_data = request.get_json()
    higherId = 0 
    for idx, task in enumerate(tasksData):
        higherId = task["id"]
        if(task["id"] > higherId):
            higherId = task["id"]
    
    req_data["id"] = higherId + 1
    tasksData.append(req_data)
    return f"Task {req_data["id"]} has been created"

@app.route('/todo/update/<id>',methods=['PUT'])
def updateTask(id):
    req_data = request.get_json()
    for idx, task in enumerate(tasksData):
        if(task["id"] == int(id)):
            taskUpdated = req_data
            tasksData.pop(idx)
            tasksData.append(taskUpdated)
            return f"Task {id} has been updated"
    return "Task not found"

@app.route('/todo/delete/<id>',methods=['DELETE'])
def deleteTask(id):
    for idx, task in enumerate(tasksData):
        if(task["id"] == int(id)):
            tasksData.pop(idx)
            return f"Task {id} has been deleted"
    return "Task not found"
