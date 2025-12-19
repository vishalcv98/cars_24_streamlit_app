from flask import Flask

app = Flask(__name__)

@app.route("/hello", methods=["GET"])
def hello():
    return "Welcome to this Flask app!"

if __name__=="__main__":
    app.run(debug=True)
