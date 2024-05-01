from flask import Flask, Blueprint, request, jsonify
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
import mysql.connector
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.secret_key = "super secret string"

students = mysql.connector.connect(
    user='root',
    password='sophie123',
    database='StudentLogin'
)

login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):
    def __init__(self, StudentID, Password):
        self.id = StudentID
        self.Password = Password

@login_manager.user_loader
def load_user(StudentID):
    cursor = students.cursor(buffered=True)
    cursor.execute("SELECT StudentID, Password FROM Students WHERE StudentID = %s", (StudentID,))
    user_data = cursor.fetchone()
    cursor.close()
    if user_data:
        return User(user_data[0], user_data[1])
    return None

@app.route('/login', methods=['POST'])
def login():
    StudentID = request.form['StudentID']
    Password = request.form['Password']
    user = load_user(StudentID)
    if user and check_password_hash(user.Password, Password):
        login_user(user)
        return jsonify(message="Login Succeed!"), 200
    return jsonify(message="Login Failed! Wrong Password"), 401

@app.route('/signup', methods=['POST'])
def signup():
    StudentID = request.form['StudentID']
    Email = request.form['Email']
    Password = generate_password_hash(request.form['password'])
    GPA = request.form['GPA']
    cursor = students.cursor(buffered=True)
    try:
        cursor.execute("INSERT INTO Students (StudentID, Email, Password, GPA) VALUES (%s, %s, %s, %s)",
                       (StudentID, Email, Password, GPA))
        students.commit()
        return jsonify(message="Signup Successful!"), 201
    except mysql.connector.IntegrityError:
        students.rollback()
        return jsonify(message="Signup Failed! StudentID already exists."), 400
    finally:
        cursor.close()

@app.route('/gpa', methods=['GET'])
@login_required
def get_gpa():
    StudentID = request.args.get('StudentID')
    cursor = students.cursor(buffered=True)
    cursor.execute("SELECT GPA FROM Students WHERE StudentID = %s", (StudentID,))
    GPA = cursor.fetchone()
    cursor.close()
    if GPA:
        return jsonify(GPA=GPA[0])
    else:
        return jsonify(message="GPA not found"), 404

@app.route('/logout')
def logout():
    logout_user()
    return "Logged out"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
