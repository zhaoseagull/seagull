from app import app
#from models import User,Post,Role_User,Role_Admin

@app.route('/')
def index():
    return "hello,zhaowei"
