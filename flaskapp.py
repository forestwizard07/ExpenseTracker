from datetime import date
from flask import Flask, jsonify, redirect , render_template, request, url_for
import psycopg2
from database import load_expenses,load_expense,add_expense,load_all,delete_expense,load_sum,fetch_analysis
#from sqlalchemy import text
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__) #the name variable will tell from where it was invoked

@app.route("/")
def render_expenses():
    curr_date = date.today()
    curr_month = curr_date.month
    print(curr_month)
    expenses = load_expenses(curr_month)
    total_sum = load_sum(curr_month)  # Rename sum to total_sum to avoid conflicts
    return render_template('home.html', trans=expenses, sum=total_sum)



@app.route("/expense/<id>")
def show_expense(id):
    expense = load_expense(id)
    trans = expense
    return render_template('expense.html',expense=trans)

@app.route("/delete/<id>")
def del_expense(id):
    expense = load_expense(id)
    trans = expense
    delete_expense(id)
    return redirect(request.referrer or url_for('render_expenses'))

@app.route("/add")
def addExpense():
    data = request.args
    #return jsonify(data)
    curr_date = date.today()
    add_expense(data,curr_date)
    return redirect(url_for('render_expenses'))

@app.route("/allExpenses")
def render_all():
    expenses = load_all()
    sum = load_sum(0)
    return render_template('alltrans.html',trans=expenses,sum=sum)

@app.route("/analysis")
def render_analysis():    
    curr_date = date.today()
    curr_month = curr_date.month
    data = fetch_analysis(curr_month)
    labels = [row[0] for row in data]
    values = [row[1] for row in data]
    return render_template('analyse.html',labels=labels,values=values,table_data=data)




if __name__ == "__main__":
    app.run(debug=True)