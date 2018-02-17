from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return "hello"

@app.route("/<range_num>")
def fib_list(range_num=5):
    myfib_list = fib(int(range_num))
    return jsonify(myfib_list)


def fib(n):
    fib_list = [0]
    a,b = 1,1
    fib_list.append(a)
    for i in range(n-1):
        a,b = b,a+b
        fib_list.append(a)
        #print(a)
    return fib_list


if __name__ == '__main__':
    app.run(debug=True)
