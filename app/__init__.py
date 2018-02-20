from flask import Flask
#import views

app = Flask(__name__)
app.config.from_object('config')

from views import views