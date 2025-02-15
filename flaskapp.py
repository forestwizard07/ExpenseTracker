from flask import Flask , render_template
app = Flask(__name__) #the name variable will tell from where it was invoked

@app.route("/")
def hello_world():
    return render_template("home.html")
if __name__ == "__main__":
    app.run(debug=True)
