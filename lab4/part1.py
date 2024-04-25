from flask import Flask
import flask_login
import mysql.connector
from flask import Blueprint, render_template, request, redirect, url_for, session
from werkzeug.security import check_password_hash, generate_password_hash

def create_app():
    app = Flask(__name__)

library = mysql.connector.connect(user = 'root',
                                    password = 'sophie123',
                                    database = 'Library')

login_manager = flask_login.LoginManager()
   
class User(flask_login.UserMixin): 
    def __init__ (self,mno, password):
        self.mno = mno
        self.password = generate_password_hash(password)

@login_manager.user_loader 
def user_finder(mno):
        cursor = library.cursor
        cursor.execute('SELECT Member Number, password from MNO = %s', (mno,) )
        user = cursor.fetchone()
        cursor.close()
        if user is not None:
            return User(user[0], user[1])
        else:
            return None
        


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5050)

