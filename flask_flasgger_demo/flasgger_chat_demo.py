from flask import Flask, jsonify, request, Blueprint
from flasgger import Swagger

# pip install flasgger -i https://pypi.tuna.tsinghua.edu.cn/simple
# 实测可用，但要注意是通过端口访问 http://localhost:5000/apidocs/

app = Flask(__name__)

swagger = Swagger(app)

blueprint1 = Blueprint('api1', __name__)


@blueprint1.route('/')
def index1():
    return 'Hello World from API 1!'


@blueprint1.route('/todos1', methods=['GET'])
def get_todos1():
    """
    Get a list of todos for API 1
    ---
    responses:
      200:
        description: A list of todos for API 1
    """
    return jsonify({
        'todos': [
            {
                'task': 'Learn Flask API 1',
                'completed': True
            },
            {
                'task': 'Learn Swagger API 1',
                'completed': False
            }
        ]
    })


app.register_blueprint(blueprint1)

blueprint2 = Blueprint('api2', __name__)


@blueprint2.route('/')
def index2():
    return 'Hello World from API 2!'


@blueprint2.route('/todos2', methods=['GET'])
def get_todos2():
    """
    Get a list of todos for API 2
    ---
    responses:
      200:
        description: A list of todos for API 2
    """
    return jsonify({
        'todos': [
            {
                'task': 'Learn Flask API 2',
                'completed': True
            },
            {
                'task': 'Learn Swagger API 2',
                'completed': False
            }
        ]
    })


app.register_blueprint(blueprint2)

if __name__ == '__main__':
    app.run(port=8700, debug=True)
