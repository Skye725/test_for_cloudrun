# from flask import Flask
# # from flask_ngrok import run_with_ngrok

# app = Flask(__name__)
# # run_with_ngrok(app)

# @app.route("/<name>")
# def home(name):
#  return f"<h1>hello {name}</h1>"

# app.run()
# # a={'hello world'}
# # return a

## index.py
import os

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({ 'status' : 'running'})

@app.route("/order", methods=["POST"])
def create_order():
    data = request.get_json()
    print('Request Data: ' + str(data))
    return jsonify({ 'msg' : 'Order Created Successfully'})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

