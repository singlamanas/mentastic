from flask import Flask, render_template, request, Response, redirect, url_for, make_response
import time
from database_handler import DBHandler
from flask_mysqldb import MySQL
import hashlib
app = Flask(__name__)

app.config['MYSQL_USER'] = "sql12614648"
app.config['MYSQL_PASSWORD'] = "1Sll3AXEpE"
app.config['MYSQL_HOST'] = "sql12.freemysqlhosting.net"
app.config['MYSQL_DB'] = "sql12614648"
app.config['MYSQL_CURSORCLASS'] = "DictCursor"

mysql = MySQL(app)
print(MySQL.connection, "Connection")

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route("/")
def home():
    username = request.cookies.get("username")
    token = request.cookies.get("token")
    cur = mysql.connection.cursor()
    cur.execute(f"SELECT * from users WHERE username='{username}'")
    results = cur.fetchall()
    if token == results[0]['password']:  
        return render_template('homepage.html', data = {'username':username})
    else:
        return render_template('homepage.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    cur = mysql.connection.cursor()
    if request.method == "GET":
        username = request.cookies.get("username")
        token = request.cookies.get("token")
        cur.execute(f"SELECT * from users WHERE username='{username}'")
        results = cur.fetchall()
        if len(results) == 1 and token == results[0]['password']:
            #user is logged in
            print("Logged in")
        else:
            print("Not logged in or User doesnot exist")

        return render_template('login.html')
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        print(username, password, "Received")
        cur.execute(f"SELECT * from users WHERE username = '{username}'")#sql query gayi hai
        results = cur.fetchall()
        if len(results) == 0:
            return render_template("login.html", feedback="User does not exist")
        else:
            if hashlib.md5((username+password+username).encode()).hexdigest() == results[0]['password']:
                resp = make_response(redirect(url_for("home")))
                resp.set_cookie("username", username)
                resp.set_cookie("token", results[0]['password'])
                return resp
            else:
                return render_template("login.html", feedback="Incorrect password")

@app.route("/signup", methods = ["GET", "POST"])
def signup():
    cur = mysql.connection.cursor()
    if request.method == "GET":
        return render_template('signup.html')
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        repass = request.form.get("re_password")
        if password != repass:
            return render_template("signup.html", feedback="Passwords don't match")
        cur.execute(f"SELECT * from users WHERE username = '{username}'")
        results = cur.fetchall()
        print(results, "Results")
        if len(results) != 0:
            print("Exists")
            return render_template("signup.html", feedback="Username already exists")
        else: 
            #INSERT INTO table_name (column1, column2, column3, ...)
            #VALUES (value1, value2, value3, ...);
            salted = username+password+username
            hash = hashlib.md5(salted.encode())

            cur.execute(f"INSERT INTO users (username, password) VALUES ('{username}', '{hash.hexdigest()}');")
            mysql.connection.commit()
            return redirect(url_for("login"))
        
@app.route("/contact", methods = ["GET", "POST"])
def contact():
    cur = mysql.connection.cursor()
    if request.method == "GET":
        return render_template('contact.html')
    else:
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        cur.execute(f"INSERT INTO contactus (name, email, message) VALUES ('{name}', '{email}', '{message}');")
        mysql.connection.commit()
        return render_template("contact.html", feedback="We've received your message")

@app.route("/men")
def men():
    return render_template('men.html')
@app.route("/trends")
def trends():
    return render_template('trends.html')
@app.route("/collections")
def collections():
    return render_template('collections.html')
@app.route("/search")
def search():
    return render_template('search.html')
@app.route("/homepage")
def homepage():
    return render_template('Homepage.html')
@app.route("/cart")
def cart():
    return render_template('cart.html')
@app.route("/product")
def product():
    return render_template('product.html')
@app.route("/sale")
def sale():
    return render_template('sale.html')
@app.route("/faq")
def faq():
    return render_template('faq.html')
@app.route("/prod_det")
def prod_det():
    return render_template('prod_det.html')
@app.route("/payment")
def payment():
    return render_template('payment.html')
@app.route("/account")
def account():
    return render_template('account.html')
@app.route("/confirm")
def confirm():
    return render_template('confirm.html')
@app.route("/thnk_fr_cont")
def thnk_fr_cont():
    return render_template('thnk_fr_cont.html')
@app.route("/recover")
def recover():
    return render_template('recover.html')
app.run(debug=True)


