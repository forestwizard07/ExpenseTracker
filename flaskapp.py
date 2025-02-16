from datetime import date
from flask import Flask, jsonify, redirect , render_template, request, url_for
import mysql.connector
from database import load_expenses,load_expense,add_expense,load_all,delete_Expense
from sqlalchemy import text
app = Flask(__name__) #the name variable will tell from where it was invoked

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

@app.route("/delete/<id>")
def del_expense(id):
    expense = load_expense(id)
    trans = expense[0]
    delete_Expense(trans)
    return redirect(request.referrer or url_for('render_expenses'))

@app.route("/add")
def addExpense():
    data = request.args
    curr_date = date.today()
    add_expense(data,curr_date)
    return redirect(url_for('render_expenses'))

@app.route("/allExpenses")
def render_all():
    expenses = load_all()
    return render_template('alltrans.html',trans=expenses)



if __name__ == "__main__":
    app.run(debug=True)