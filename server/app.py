#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return f"{parameter}"

@app.route("/count/<int:parameter>")
def count(parameter):
    numbers = ''
    for number in range(parameter):
        numbers += f'{number}\n'
    return numbers

@app.route("/math/<num1>/<operation>/<num2>")
def math(num1,operation,num2):
    int_num1 = int(num1) 
    int_num2 = int(num2) 
    if operation == "+":
        return f"{int_num1 + int_num2}"
    elif operation == "-":
        return f"{int_num1 - int_num2}"
    elif operation == "*":
        return f"{int_num1 * int_num2}"
    elif operation == "div":
        return f"{int_num1 / int_num2}"
    else:
        return f"{int_num1 % int_num2}"


if __name__ == '__main__':
    app.run(port=5555, debug=True)

