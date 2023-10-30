from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form.get("name")
    input_age = request.form.get("age")
    input_city = request.form.get("city")
    return render_template("hello.html",
                           name=input_name,
                           age=input_age,
                           city=input_city)


def process_query(query):
    if "dinosaurs" in query:
        return "Dinosaurs ruled the Earth 200 million years ago"
    elif "name" in query:
        return "Ak_Tiril"
    elif "numbers" in query:
        return get_largest_number(query)
    else:
        return "Unknown"


@app.route("/query")
def query():
    return process_query(request.args.get('q', default="", type=str))


def get_largest_number(str1):
    res = []
    for i in str1.split():
        if i.isdigit():
            res.append(i)
    return str(max(res))
