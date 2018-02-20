from fibonacci import fibonacci
from flask import Flask, request
from flask import render_template
from static import status

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/fibonacci')
def fib_list():
    if 'num' in request.args:
        try:
            range_num = int(request.args.get('num'))
        except ValueError:
            response = 'please submit only a positive integer, no special characters.'
            return response, status.HTTP_403_FORBIDDEN
        if range_num < 1 or range_num > 10000:
            response = 'improper data provided'
            return response, status.HTTP_403_FORBIDDEN
        if range_num > 1:
            myfib_list = fibonacci.fibonacci(range_num)
        # return jsonify(myfib_list)
            return render_template("fibonacci.html", display_range_num=range_num, fibonacci_list=myfib_list)
    else:
        response = 'Improper request'
        return response, status.HTTP_400_BAD_REQUEST


# def fib(n):
#     fib_list = [0]
#     a,b = 1,1
#     fib_list.append(a)
#     for i in range(n-2):
#         a,b = b,a+b
#         fib_list.append(a)
#         #print(a)
#     return fib_list


if __name__ == '__main__':
    app.run(debug=True)
