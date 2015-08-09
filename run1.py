import datetime
import hashlib
import string,random
import config1
from flask import Flask,jsonify,request

from fkmysql1 import db,app,Player

def get_user_id(username):
    p=Player.query.filter_by(username=username).first()
    if p is not None:
        return p
    return None

def get_userid_by_email(email):
    p  = Player.query.filter_by(email=email).first()
    if p  is not None:
       return p
    return None

def get_user_key(key):
    p  = Player.query.filter_by(activation_key=key).first()
    if p  is not None:
       return p
    return None

@app.route('/')
def nototell():
    return "not to tell"

@app.route('/users')
def list_players():
    players=Player.query.all()
    d={}
    for p in players:
        app.logger.debug(p.username)
        a=p.username
    return "hello,player %s"% (a)

if __name__ == '__main__':
    app.debug = True
    #app.run(host='0.0.0.0')
    app.run()
