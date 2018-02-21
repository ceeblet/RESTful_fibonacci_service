from app import app
from app import fibonacci
from flask import render_template, request
from static import status


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
        if range_num >= 1:
            myfib_list = fibonacci.fibonacci(range_num)
            return render_template("fibonacci.html", display_range_num=range_num, fibonacci_list=myfib_list)
    else:
        response = 'Improper request'
        return response, status.HTTP_400_BAD_REQUEST

