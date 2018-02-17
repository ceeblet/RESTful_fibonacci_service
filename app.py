from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def index():
    return "hello"


@app.route("/fibonacci")
def fib_list():
    if 'num' in request.args:
        range_num = int(request.args.get('num'))
        if range_num > 1:
            myfib_list = fib(range_num)
            return jsonify(myfib_list)
        else:
            return "Not a valid number"


def fib(n):
    fib_list = [0]
    a,b = 1,1
    fib_list.append(a)
    for i in range(n-2):
        a,b = b,a+b
        fib_list.append(a)
        #print(a)
    return fib_list


if __name__ == '__main__':
    app.run(debug=True)
