import sqlite3


def connect():
    conn = sqlite3.connect("goodreads.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    # creates tables and sets keys(columns) in database
    conn.commit()
    conn.close()


# input for the 4 entries
def add_Book(title, author, year, isbn):
    conn = sqlite3.connect("goodreads.db")
    cur = conn.cursor()
    conn.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
    conn.commit()
    conn.close()

def all_Books():
    conn = sqlite3.connect("goodreads.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows
 
def search(title=" ", author=" ", year=" ", isbn=" "): #passed empty values so ueser can input 1-4 entries
    conn = sqlite3.connect("goodreads.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?", (title,author,year,isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete_Book(id):
    conn = sqlite3.connect("goodreads.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id = ?", (id,))
    conn.commit()
    conn.close()

def update_List(id, title, author, year, isbn):
    conn = sqlite3.connect("goodreads.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?", (title, author, year, isbn, id))
    conn.commit()
    conn.close()

        


    



    

connect()
#add_Book("POOP","Cj", 1111, 11111)
#delete_Book(24)
#update_List(25, "Moon", "ggg", 445453, 1213121)
print(search(author = "John Smith"))
