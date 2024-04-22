import mysql.connector
from mysql.connector import Error

# Connect to Server
mydb = mysql.connector.connect(
                            host = 'localhost',
                            user ='root',
                            password ='sophie123',
                            database = "Library"
)


cursor = mydb.cursor()
cursor.execute("CREATE DATABASE Library")


BookRecord = """CREATE TABLE IF NOT EXISTS BOOKRECORD (
                Bno INT AUTO_INCREMENT PRIMARY KEY,
                Bname VARCHAR(20) NOT NULL,
                Auth VARCHAR(20) NOT NULL,
                Price INT,
                Publ VARCHAR(20) NOT NULL,
                QTY INT,
                Date_of_Purchase DATE
                )
                """
cursor.execute(BookRecord)

# Create the Issue table if not exists
Issue= """CREATE TABLE IF NOT EXISTS Issue (
            Bno INT,
            Mno INT, 
            d_o_issue DATE, 
            d_o_ret DATE
            )
            """
cursor.execute(Issue)

# Create the Member table if not exists
members = """CREATE TABLE IF NOT EXISTS Members(    
            Mno INT,
            Mname VARCHAR(20) NOT NULL, 
            Date_of_Membership DATE, 
            Addr VARCHAR(24),
            Mob VARCHAR(10)
            )
            """
cursor.execute(members)
        
print("Tables created successfully")


#Add book function # -10pts, to avoid any errors, try to implement a try-except block to output any errors.
def addBook(connection, Bname, Auth, Price, Publ, Date_of_Purchase):
    
    cursor = connection.cursor()
    sql_query = """INSERT INTO Bookrecord (Bname, Auth, Price, Publ, Date_of_Purchase) 
                        VALUES (%s, %s, %s, %s, %s)"""
    book_data = (Bname, Auth, Price, Publ, Date_of_Purchase)
    cursor.execute(sql_query, book_data)
    connection.commit()
    print("Book added successfully")
  
cursor.execute()

#Delete book function 
def deleteBook(connection, Bno):
    cursor = connection.cursor()
    sql_query = "DELETE FROM Bookrecord WHERE Bno = %s"
    cursor.execute(sql_query, (Bno,))
    connection.commit()
    if cursor.rowcount > 0:
        print("Book deleted successfully")
    else:
        print("No book found with the given book number")

cursor.execute()
 
#Search book function 
def searchBook(connection, Bno):
    cursor = connection.cursor()
    sql_query = "SELECT * FROM Bookrecord WHERE Bno = %s"
    cursor.execute(sql_query, (Bno,))
    book = cursor.fetchone()
    if book:
        print("Book details:")
        print(f"Book Number: {book[0]}")
        print(f"Book Name: {book[1]}")
        print(f"Author: {book[2]}")
        print(f"Price: {book[3]}")
        print(f"Publisher: {book[4]}")
        print(f"Date of Purchase: {book[5]}")
    else:
        print("No book found with the given book number")
    
#Update book section 
def updateBook(connection, Bno, Bname, Auth, Price, Publ, Date_of_Purchase):
    cursor = connection.cursor()
    sql_query = """UPDATE Bookrecord 
                        SET Bname = %s, Auth = %s, Price = %s, Publ = %s, Date_of_Purchase = %s 
                        WHERE Bno = %s"""
    book_data = (Bname, Auth, Price, Publ, Date_of_Purchase, Bno)
    cursor.execute(sql_query, book_data)
    connection.commit()
    if cursor.rowcount > 0:
        print("Book updated successfully")
    else:
        print("No book found with the given book number")
    


addBook(mydb, "the little mermaid", "sophia", 20, "Jade", "2000-20-12")
deleteBook(mydb, 1)
searchBook(mydb, 2)
updateBook(mydb, 3, "TLM", "sophG", 30, "Jade", "2003-23-01")
