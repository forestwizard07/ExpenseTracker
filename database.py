import mysql.connector
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",     # Change if using a remote database
        user="root",
        password="Chintamani1#",
        database="expenses"
    )
def load_expenses():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True) 
    cursor.execute("SELECT * FROM expenselog ORDER BY id DESC LIMIT 10;")
    expenses = cursor.fetchall()  
    return expenses

def load_expense(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True) 
    cursor.execute("SELECT * FROM expenselog WHERE id = %s", (id,))
       
    expenses = cursor.fetchall() 
    if len(expenses) == 0:
        return None
    else:
        return expenses
    
def add_expense(data,curr):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True) 
    cursor.execute("insert into expenselog (amount,comments,dateofExpense,dateofLog) values (%s,%s,%s,%s)",(data['amount'],data['desc'],data['date'],curr))
    conn.commit()
    conn.close()

def delete_Expense(trans):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True) 
    cursor.execute("delete from expenselog where id = %s",(int(trans['id']),))
    cursor.execute("ALTER TABLE expenselog AUTO_INCREMENT = 1")
    conn.commit()
    conn.close()

def load_all():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True) 
    cursor.execute("SELECT * FROM expenselog ORDER BY dateofExpense DESC;")
    expenses = cursor.fetchall()  
    return expenses



