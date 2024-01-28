from flask import Flask
from flask import jsonify
from flask import request
from connect import pgConnect
from dbOperations import dbOperations
import json
from flask_cors import CORS

dbConnection = pgConnect().dbConnect()

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
    sql = "SELECT * FROM tasks.task"
    tasks = dbOperations.select(dbConnection,sql)
    return jsonify(tasks)

@app.route('/todo/create',methods=['POST'])
def createTask():
    req_data = request.get_json()
    
    sql = """
    INSERT into tasks.task (description,status) 
    values('%s','%s') RETURNING id;
    """ % (req_data["description"], req_data["status"])
    created = dbOperations.insert(dbConnection,sql)
    return f"Task {created} has been created"

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
