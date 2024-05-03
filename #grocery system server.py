# This submission missed two required elements: a README file explaining the app's functionalities; a database file that separates the database models from the server views. -15pts

#grocery system server
from flask import Flask, request, session, redirect, url_for, render_template, flash
from werkzeug.security import check_password_hash, generate_password_hash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'super secret key' 

# missing the declaration of session object that keeps track of the user status and is constantly used in followings. -5pts

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="sophie123",
        database="grocerysystem"
    )

@app.route('/')
def index():
    if 'user_id' in session:
        return 'Logged in as %s' % session['user_id']
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = connect_db()
        cursor = db.cursor()
        cursor.execute("SELECT employee_name, password FROM employee WHERE employee_name = %s", (username,))
        user = cursor.fetchone()
        if user and check_password_hash(user[1], password):
            session['user_id'] = user[0]
            return redirect(url_for('index'))
        flash('Invalid username or password')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))

@app.route('/protected')
#missing @flask_login.login_required, which protected this route to be available for authenticated user only; -5pts
def protected():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return 'Protected area'

if __name__ == '__main__':
    app.run(debug=True)
    
