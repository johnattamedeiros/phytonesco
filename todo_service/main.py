from flask import Flask
from flask import jsonify
from flask import request
from connect import pgConnect
from dbOperations import dbOperations
from flask_cors import CORS

dbConnection = pgConnect().dbConnect()
app = Flask(__name__)
app.run(debug=True)
CORS(app)


@app.route('/')
def mainRoute():
    return 'Welcome to pythonesco API'

@app.route('/tasks/get',methods=['GET'])
def getTasks():
    sql = "SELECT * FROM tasks.task"
    tasks = dbOperations.select(dbConnection,sql)
    return jsonify(tasks)

@app.route('/tasks/create',methods=['POST'])
def createTask():
    req_data = request.get_json()
    
    sql = """
    INSERT into tasks.task (description,status) 
    values('%s','%s') RETURNING id;
    """ % (req_data["description"], req_data["status"])
    created = dbOperations.insert(dbConnection,sql)
    return f"Task {created} has been created"

@app.route('/tasks/update/<id>',methods=['PUT'])
def updateTask(id):
    req_data = request.get_json()
    sql = """
    UPDATE tasks.task SET description = '%s',status = '%s'
    WHERE id = '%s' RETURNING id
    """ % (req_data["description"], req_data["status"],id)
    updatedTask = dbOperations.update(dbConnection,sql,id)
    return jsonify(updatedTask)

@app.route('/tasks/delete/<id>',methods=['DELETE'])
def deleteTask(id):
    sql = """
    DELETE FROM tasks.task 
    WHERE id = '%s'
    """ % (id)
    deletedTask = dbOperations.delete(dbConnection,sql,id)
    return jsonify(deletedTask)
