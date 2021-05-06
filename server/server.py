import flask
from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/hello')
def hi():
    return "hello"

if __name__ == "__main__":
    print("starting python server")
    app.run()