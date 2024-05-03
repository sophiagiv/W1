# This GUI doesn't manage the database by talking to the server; 
# the respective url calls are missing under login(), insert_record() and add_product() functions. -10pts


#final grocery store system main 
import mysql.connector
from mysql.connector import Error
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from werkzeug.security import check_password_hash, generate_password_hash

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="sophie123",
        database="grocerysystem"
    )

employee = """CREATE TABLE IF NOT EXISTS employee (
    employee_name VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    PRIMARY KEY (employee_name)
);
"""

product = """CREATE TABLE IF NOT EXISTS products (
    product_id INT AUTO_INCREMENT,
    product_name VARCHAR(255) NOT NULL,
    PRIMARY KEY (product_id)
);
"""

class MainWindow:
    def __init__(self, window):
        self.window = window
        self.window.title("Grocery Store System")
        self.window.geometry("300x300")
        self.window.config(bg='light yellow')
        original_image = Image.open('/Users/sophiagiovannone/Desktop/apple.png')
        resized_image = original_image.resize((100, 100))
        self.apple_image = ImageTk.PhotoImage(resized_image)

        self.image_label = tk.Label(self.window, image=self.apple_image)
        self.image_label.pack(pady=20) 

        self.setup_login_screen()

    def setup_login_screen(self):
        self.login_frame = tk.Frame(self.window, bg='light yellow')
        self.login_frame.pack()

        self.employee_name_label = tk.Label(self.login_frame, text="Employee Name:", fg='red', bg='light yellow')
        self.employee_name_label.pack()

        self.employee_name_entry = tk.Entry(self.login_frame)
        self.employee_name_entry.pack()

        self.password_label = tk.Label(self.login_frame, text="Password:", fg='red', bg='light yellow')
        self.password_label.pack()

        self.password_entry = tk.Entry(self.login_frame, show="*", fg='red', bg='light yellow')
        self.password_entry.pack()

        self.login_button = tk.Button(self.login_frame, text="Login", command=self.login, fg='red', bg='light yellow')
        self.login_button.pack(pady=10)

    def login(self):
        employee_name = self.employee_name_entry.get()
        password = self.password_entry.get()
        db = connect_db()
        if db:
            cursor = db.cursor()
            try:
                cursor.execute("SELECT * FROM employee WHERE employee_name=%s", (employee_name,))
                result = cursor.fetchone()
                if result and check_password_hash(result[1], password):
                    self.login_frame.pack_forget()
                    self.setup_product_addition_screen()
                else:
                    messagebox.showerror("Login Failed", "Invalid employee name or password")
            except mysql.connector.Error as e:
                messagebox.showerror("Database Error", str(e))
            finally:
                cursor.close()
                db.close()
        else:
            messagebox.showerror("Database Error", "Failed to connect to the database.")
    
    def add_product(self):
        self.new_window = tk.Toplevel(self.window)
        self.new_window.title("Add New Product")
        self.new_window.geometry('300x200')
        self.new_window.config(bg='light yellow')

        self.name_label = tk.Label(self.new_window, text='Product Name:', fg='red', bg='light yellow')
        self.name_label.pack()

        self.name_entry = tk.Entry(self.new_window)
        self.name_entry.pack()

        self.product_id_label = tk.Label(self.new_window, text="Product ID:", fg='red', bg='light yellow')
        self.product_id_label.pack()

        self.id_entry = tk.Entry(self.new_window)
        self.id_entry.pack()

        self.button = tk.Button(self.new_window, text='Insert Product', command=self.insert_records, fg='red', bg='light yellow')
        self.button.pack(pady=10)

    def insert_records(self):
        db = connect_db()
        if db:
            cursor = db.cursor()

            product_name = self.name_entry.get()
            product_id = self.id_entry.get()

            if product_name and product_id:
                try:
                    cursor.execute("INSERT INTO products (product_name, product_id) VALUES (%s, %s)", (product_name, product_id))
                    db.commit()
                    messagebox.showinfo("Success", "Product Added Successfully")
                except mysql.connector.Error as e:
                    messagebox.showerror("Database Error", str(e))
                finally:
                    cursor.close()
                    db.close()
            else:
                messagebox.showerror("Input Error", "Please provide both product name and ID.")
        else:
            messagebox.showerror("Database Error", "Unable to connect to the database.")
        
    def search_product(self):
        db = connect_db()
        if db:
            cursor = db.cursor()
            search_term = self.search_entry.get()
            query = "SELECT * FROM products WHERE product_name LIKE %s"
            cursor.execute(query, ('%' + search_term + '%',))
            result = cursor.fetchall()
            if result:
                messagebox.showinfo("Search Results", "\n".join([str(row) for row in result]))
            else:
                messagebox.showinfo("Search Results", "No matching products found.")
            cursor.close()
            db.close()
        else:
            messagebox.showerror("Database Error", "Failed to connect to the database.")

if __name__ == "__main__":
    window = tk.Tk()
    main_window = MainWindow(window)
    window.mainloop()
