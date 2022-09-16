from flask import jsonify
from flask import render_template
from flask import request
from flask import Flask


app = Flask(__name__)




@app.route('/')
def index():
    return render_template('index_2.html')


@app.route('/login', methods=["POST","GET"])
def login():
    if request.method == "POST":
        h1 = request.form['red']
        s1 = request.form['green']
        v1 = request.form['blue']

        h2 = request.form['red2']
        s2 = request.form['green2']
        v2 = request.form['blue2']
        print("h1 =",h1,"s1 =",s1,"v1=",v1)
        print("h2 =",h2,"s2 =",s2,"v2=",v2)
    else:
        print("Method = GET!")
        return ''
    return ''

if __name__ == "__main__":
    #app.run(host="192.168.0.105", port=8086, debug=True)
    app.run(debug=True)
