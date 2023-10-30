from flask import Flask, render_template, request
import re


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
    elif "largest" in query:
        numlist = re.findall(r'\d+', query)
        return str(max(list(map(int, numlist))))
    elif "multiplied" in query:
        numlist = re.findall(r'\d+', query)
        return str(int(numlist[0]) * int(numlist[1]))
    elif "plus" in query:
        numlist = [int(i) for i in re.findall(r'\d+', query)]
        return str(numlist[0] + numlist[1])
    elif "minus" in query:
        numlist = [int(i) for i in re.findall(r'\d+', query)]
        return str(numlist[0] - numlist[1])
    elif "primes" in query:
        numlist = [int(i) for i in re.findall(r'\d+', query)]
        for num in numlist:
            if (is_prime(num)):
                return str(num)
    else:
        return "Unknown"


@app.route("/query")
def query():
    return process_query(request.args.get('q', default="", type=str))


def is_prime(num):
    flag = True
    for i in range(2, num):
        if num % i == 0:
            flag = False
    return flag
