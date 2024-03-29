# RESTful_fibonacci_service
a wee RESTful fibonacci web service

This web service accepts a number, n, as input and returns the first n Fibonacci numbers, starting from 0

For example:
An input of 5 will return ```[0,1,1,2,3]```

### To Install:

It is best to perform the following commands in a virtual environment. 
This service uses python >=3.4

Refer to the following web page for instructions on setting up a virtual environment in python 3
https://docs.python.org/3/library/venv.html

- create a directory to install into
- activate your virtual environment
- clone this git repo
- (if you downloaded the zip, unpack the zip file)
- cd into the repo direcotry
- type pip install -r requirements.txt
- type python3 run.py
- you should see the following output:
```
  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
- Open your browser of choice and type or cut and paste the address http://127.0.0.1:5000/ into the address bar

### Usage:
```
GET /fibonacci?num=[int]
```
