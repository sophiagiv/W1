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


bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        mno = request.form.get('mno')
        password = request.form.get('password')
        
        user = request.User.query.filter_by(mno=mno).first()
        if user and check_password_hash(user.password, password):
            session['mno'] = mno
            return redirect(url_for('auth.protected'))
        else:
            return redirect(url_for('auth.invalid'))

    return render_template('login.html')

@bp.route('/protected')
def protected():
    mno = session.get('mno')
    if mno:
        user_books = request.get_user_books(mno)
        return render_template('protected.html', user_books=user_books)
    else:
        return redirect(url_for('auth.login'))

@bp.route('/logout')
def logout():
    session.pop('mno', None)
    return redirect(url_for('auth.login'))

@bp.route('/invalid')
def invalid():
    return 'Invalid login'
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
        