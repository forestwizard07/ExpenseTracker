from flask import Flask, jsonify , render_template
app = Flask(__name__) #the name variable will tell from where it was invoked

TRANSACTIONS = [
    {
        'id':1,
        'amount':20000,
        'desc': 'Goa Trip',
        'date': '27-01-2025'
    },
    {
        'id':2,
        'amount':4000,
        'desc': 'Fan',
        'date': '3-02-2025'
    },
    {
        'id':3,
        'amount':30,
        'desc': 'Ice cream',
        'date': '15-02-2025'
    },
    {
        'id':4,
        'amount':40,
        'desc': 'Scale',
        'date': '15-02-2025'
    }
]

@app.route("/")
def hello_world():
    return render_template("home.html",trans=TRANSACTIONS)

@app.route("/api/transactions")
def list_transactions():
    return jsonify(TRANSACTIONS)

if __name__ == "__main__":
    app.run(debug=True)
