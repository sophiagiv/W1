from werkzeug.security import check_password_hash, generate_password_hash
from flask import Flask, request
import flask_login
import mysql.connector 
from flask import Blueprint
from flask import Flask 
import mysql.connector

bp = Blueprint('auth', __name__,desktop_folder = 'lab4') 


def create_app():
    app = Flask(__name__)
    login_manager.init_app(app)
    app.register_blueprint(bp)
  
library = mysql.connector.connect(user = 'root',
                                    password = 'sophie123',
                                    database = 'Library')


login_manager = flask_login.LoginManager()

class User(flask_login.UserMixin): 
    def __init__ (self,id, mno, password):
        self.id = id
        self.mno = mno
        self.password = generate_password_hash(password)

    def __init__(self, mno, password):
        self.mno = mno
        self.password = generate_password_hash(password)

    def get_user_books(mno):

        return app
    
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5050)
