from flask import Blueprint, request, jsonify

task_blueprint = Blueprint('task', __name__) #nama blueprint nya bebas


# GET /task
# GET /task/index
# POST /task

tasks =[] # ini list nya


@task_blueprint.route('/tasks', methods=['GET'])
def get_tasks():
    """
    Get all tasks
    ---
    tags:
      - Tasks
    responses:
      200:
        description: List of tasks
        schema:
          type: object
          properties:
            task:
              type: array
              items:
                type: string
    """
    
    return {'task' : tasks}, 200

@task_blueprint.route('/tasks/<int:index>', methods=['GET'])
def get_task(index):
    """
    Get single task
    ---
    tags:
      - Tasks
    parameters:
      - name: index
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Single task
      404:
        description: Task not found
    """
    try:
        task = tasks[index]
        return {'task' : task}, 200
    except IndexError:
        return {'error' : 'Task not found'}, 400
    
@task_blueprint.route('/tasks', methods=['POST'])
def add_task():
    """
    Create a new task
    ---
    tags:
      - Tasks
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - task
          properties:
            task:
              type: string
              example: belajar flask swagger
    responses:
      201:
        description: Task created successfully
        schema:
          type: object
          properties:
            message:
              type: string
              example: Task Added
            task:
              type: string
              example: belajar flask swagger

      400:
        description: Invalid request body
        schema:
          type: object
          properties:
            error:
              type: string
              example: task is not provided
    """
    data = request.get_json()
    task = data.get('task')
    if task:
        tasks.append(task)
        return jsonify({'message' : 'Task Added', 'task' : task}), 201
    else:
        return jsonify({'error' : 'task is not provided'}), 400
    
