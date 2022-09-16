from flask import jsonify
from flask import render_template
from flask import request
from flask import Flask


app = Flask(__name__)




@app.route('/')
def index():
    return render_template('index_2.html')

@app.route("/add", methods=["POST"])
def add():
    a = request.form.get("a", 0, type=float)
    b = request.form.get("b", 0, type=float)
    return jsonify(result=a + b)

@app.route('/login', methods=["POST","GET"])
def login():
    if request.method == "POST":
        red = request.form['red']
        green = request.form['green']
        blue = request.form['blue']
        print(red,green,blue)
    else:
        print("Method = GET!")
        return ''
    return ''

if __name__ == "__main__":
    #app.run(host="192.168.0.105", port=8086, debug=True)
    app.run(debug=True)
