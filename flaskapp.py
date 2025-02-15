from flask import Flask, jsonify, redirect , render_template, request, url_for
import mysql.connector
from database import load_expenses,load_expense,add_expense
from sqlalchemy import text
app = Flask(__name__) #the name variable will tell from where it was invoked

'''def get_db_connection():
    return mysql.connector.connect(
        host="localhost",     # Change if using a remote database
        user="root",
        password="Chintamani1#",
        database="expenses"
    )'''

@app.route("/")
def render_expenses():
    expenses  = load_expenses()
    return render_template('home.html', trans=expenses)


@app.route("/api/transactions")
def list_transactions():
    expenses = load_expenses()
    return jsonify(expenses)

@app.route("/expense/<id>")
def show_expense(id):
    expense = load_expense(id)
    trans = expense[0]
    return render_template('expense.html',expense=trans)

@app.route("/add")
def addExpense():
    data = request.args
    add_expense(data)
    return redirect(url_for('render_expenses'))
    '''add_expense(amt,desc,date)
    expenses  = load_expenses()
    return render_template('home.html', trans=expenses)'''



if __name__ == "__main__":
    app.run(debug=True)