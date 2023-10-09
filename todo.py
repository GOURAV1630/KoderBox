import uuid
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database (a dictionary) for storing tasks
tasks = {
    1: {
        "id": 1,
        "description": "Complete the project report",
        "due_date": "2023-10-15",
        "status": "Incomplete"
    },
    2: {
        "id": 2,
        "description": "Buy groceries",
        "due_date": "2023-09-30",
        "status": "Incomplete"
    },
    3: {
        "id": 3,
        "description": "Prepare for the presentation",
        "due_date": "2023-10-05",
        "status": "Incomplete"
    }
}

task_id_counter = 1

@app.route('/tasks', methods=['GET'])
def get_tasks():
    """Get all tasks"""
    return jsonify(list(tasks.values()))

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """Ek specific task id do"""
    task = tasks.get(task_id)
    if task is None:
        print(' ')
        # abort(404) #When that id or task is not found
    return jsonify(task)

# @app.route('/tasks', methods=['POST'])
# def create_task():
#     """Create a new task"""
#     global task_id_counter
#     data = request.json
#     # print(data)
#     task_id = task_id_counter
#     task = {
#         'id':task_id,
#         'title': data['title'],
#         'completed': False
#     }
#     tasks[task_id] = task
#     task_id_counter += 1
#     return jsonify(task), 201 

@app.route('/tasks', methods=['POST'])
def create_task():
    """Create a new task"""
    data = request.json
    
    # Generate a unique ID for the new task
    # task_id = str(uuid.uuid4())
    
    task = {
        'id': data['id'],
        'title': data['title'],
        'completed': data['completed']
    }
    tasks[data['id']] = task
    return jsonify(task), 201

@app.route('/tasks/<int:task_id>', methods=['PATCH'])
def update_task(task_id):
    """Update a task by ID"""
    task = tasks.get(task_id)
    if task is None:
        abort(404)
    data = request.json
    if 'title' in data:
        task['title'] = data['title']
    if 'completed' in data:
        task['completed'] = data['completed']

    tasks[task_id] = task
    return jsonify(task)

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Delete a task by ID""" 
    task = tasks.get(task_id)
    if task is None:
        abort(404)  # Task not found
    
    del tasks[task_id]
    return '', 204  # 204 No Content


if __name__ == '__main__':
    app.run(debug=True)

