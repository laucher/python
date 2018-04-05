# coding:utf-8


from flask import Flask,render_template,request

app = Flask(__name__);

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/test-get",methods=["GET"])
def test_get():
    return "test_get"

@app.route("/test-post",methods=["POST"])
def test_post():
    return "test_post"

@app.route("/add",methods=["POST"])
def add():
    a = request.args.get("num1")
    b = request.args.get("num2")
    return str(int(a)+int(b))

app.run();






