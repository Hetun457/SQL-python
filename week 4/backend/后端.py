from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)

CORS(app)


@app.route("send", methods=["POST"])
def send():

    data = request.json

    value = data["xxx"]

    return jsonify({
        "message": "你的参数是：" + value
    })

@app.route("/send2", methods=["POST"])
def send2():

    data = request.json

    body_value = data["body"]

    param_value = request.args.get("param")

    return jsonify({
        "message": "body中的参数是：" + body_value +
                   "，param中的参数是：" + param_value
    })

if __name__ == "__main__":
    app.run(port=5000)
