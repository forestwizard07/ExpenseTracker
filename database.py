# db.py
import psycopg2
import os

def get_db_connection():
    return psycopg2.connect(os.environ.get('DATABASE_URL'))


def load_expenses(month):
    conn = get_db_connection()
    cursor = conn.cursor()  # Use RealDictCursor here
    cursor.execute("SELECT * FROM expenselog WHERE EXTRACT(MONTH FROM dateofExpense) = %s ORDER BY dateofExpense DESC", (month,))
    expenses = cursor.fetchall()
    conn.close()
    print(f"Fetched expenses: {expenses}")  # Debugging line
    return expenses


def load_sum(month):
    conn = get_db_connection()
    cur = conn.cursor()
    if month == 0:
        cur.execute("SELECT SUM(amount) FROM expenselog;")
    else:
        cur.execute("SELECT SUM(amount) FROM expenselog WHERE EXTRACT(MONTH FROM dateofExpense) = %s;", (month,))
    total = cur.fetchone()
    conn.close()
    print(total[0])
    return total[0]  # return the numeric value

def load_expense(expense_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM expenselog WHERE id = %s;", (expense_id,))
    expense = cur.fetchone()
    conn.close()
    
    if expense is None:
        return None  # or handle this case as needed
    
    # Return the full tuple or create a dictionary to make accessing easier
    return {
        'id': expense[0],
        'amount': expense[1],
        'comments': expense[2],
        'dateofExpense': expense[3],
        'dateofLog': expense[4],
        'mode': expense[5]
    }
def add_expense(data, curr):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenselog (amount, comments, dateofExpense, dateofLog, mode) VALUES (%s, %s, %s, %s, %s)",
                   (data['amount'], data['desc'], data['date'], curr, data['mode']))
    conn.commit()  # Make sure this commit is executed
    conn.close()


def delete_expense(expense_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM expenselog WHERE id = %s;", (expense_id,))
    conn.commit()
    conn.close()

def load_all():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM expenselog ORDER BY dateofExpense DESC;")
    expense = cur.fetchall()
    conn.close()
    return expense