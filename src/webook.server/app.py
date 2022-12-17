from flask import Flask, request, json

app = Flask(__name__)


@app.route("/webhook", methods=["POST"])
def webhook():
    # print(f'Request: {request.json}')
    if request.method == "POST":
        print("Data received from Webhook is: ", request.json)
        return "Webhook received!"


@app.route("/event", methods=["POST"])
def event():
    # print(f'Request: {request.json}')
    if request.method == "POST":
        print("Data received from Event is: ", request.json)
        return "Event received!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
