from flask import flask
app = Flask(__name__)

@app.route("/")
def text():
    return "Hello from Docker pipelinie CI/CD"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)