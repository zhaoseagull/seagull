import flask
import os
from flask_sqlalchemy  import SQLAlchemy
from config import basedir


app=flask.Flask(__name__)
app.config.from_object('config')
db=SQLAlchemy(app)


import models
import views
