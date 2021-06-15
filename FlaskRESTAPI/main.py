from flask import Flask, jsonify

"""jsonify will format our result in a formal way and 
submit it to the chrome in form of JSON of Javascript.
Json in JavaScript is like Dictionary in pYhton."""
app = Flask(__name__)


@app.route('/')
@app.route("/home")
def hello_world():
    return "Hello, World!"


@app.route('/odd_even/<int:num>')
def odd_ever(num):
    if num % 2 == 0:
        print(f"{num} is an EVEN number.")
        result = {
            "Number": num,
            "Even": True,
            "Other Number": [5, 4, 3, 6],
            "Coder": "Jabir Aziz"
        }
        return jsonify(result)
    else:
        print(f"{num} is an Odd number.")
        result = {
            "Number": num,
            "ODD": True,
            "Other Number": [9, 6, 5, 3, 6],
            "Coder": "Jabir Aziz"
        }
        return jsonify(result)


"""to make our result more attractive on screen then open up google and 
search for jsonify formatter chrome and add it to the chrome."""

if __name__ == "__main__":
    app.run(debug=True)
