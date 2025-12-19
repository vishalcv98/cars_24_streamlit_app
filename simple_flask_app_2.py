from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/greet", methods=["GET","POST"])
def greet():
    
    # I will do some processing or transformation on the data
    if request.method == "GET":
        name = request.args.get("name","user")
        age = request.args.get("age",15)
    else:
        data = request.json
        name = data.get("name","user")
        age = data.get("age",15)


    

    res = f"Hello, {name}! You are {age} years old."

    return jsonify({"message":res})


if __name__=="__main__":
    app.run(debug=True)