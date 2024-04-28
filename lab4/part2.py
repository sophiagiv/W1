from flask import Blueprint, render_template, request, redirect, url_for, session
import flask_login
from werkzeug.security import check_password_hash
import database  # import part1; incorrect module name -2pts


library = database.library #part1.library

# Missing the member signup viw function; - 8pts.

bp = Blueprint('auth', __name__)  #

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        mno = request.form.get('mno')
        password = request.form.get('password')
        
        user = request.User.query.filter_by(mno=mno).first() #User has yet been imported; user= part1.user_finder(mno); -4pts
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
