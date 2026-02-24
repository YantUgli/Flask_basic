from flask import Flask, request, jsonify
from datetime import datetime
from views.task_view import task_blueprint
from flasgger import Swagger
from views.user import users_blueprint

app = Flask(__name__)
# Blueprint start
app.register_blueprint(task_blueprint)
app.register_blueprint(users_blueprint)
# Blueprint end

swagger = Swagger(app)

# middleware untuk debugging
@app.before_request
def start_timer():
    request.start_time = datetime.now()
    # ngehck path
    # if request.path in ["/books", "/tasks"]:
    #     print('this is book or task')
    # else:
    #     return

@app.after_request
def log_time(response):
    end_time = datetime.now()
    request_time = (end_time - request.start_time).total_seconds()
    print(f'request time: {request_time} seconds')
    return response

# route
# functions / views

@app.route("/", methods=['GET']) #tulisan http method nya boleh kecil maupun besar. != sesitive case, but better capital
def index():
    response = {'message':'this main route'}
    return jsonify(response), 200 # bisa kasih tau code nya


@app.route('/books', methods=['GET', 'POST'])
def handle_books():
    if request.method == "POST":
        # Create book here
        return jsonify({'message':'Create a book'})
    else:
        # Retrieve list of books here
        return jsonify({'message':'return list of books'})
    

@app.errorhandler(404)
def not_found(error):
    return jsonify(error=str(error)), 404

