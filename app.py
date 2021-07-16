from flask import Flask, request,jsonify        # import flask
app = Flask(__name__)             # create an app instance


from models import Schema
from Service import ToDoService

@app.route("/todo",methods=["POST"]) # at the end point /
def create_todo():
    return jsonify(ToDoService().create(request.get_json()))

@app.route("/")                   # at the end point /
def hello():                      # call method hello
    return "Hello World!"


if __name__ == "__main__":        # on running python app.py
    Schema()
    app.run(debug=True)