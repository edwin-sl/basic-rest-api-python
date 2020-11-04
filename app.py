from flask import Flask
from routes.users import users_blueprint
from routes.todos import todos_blueprint

app = Flask(__name__)
app.register_blueprint(users_blueprint)
app.register_blueprint(todos_blueprint)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
