from flask import Flask, render_template,request, Response, redirect, url_for, make_response, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
# from login import app
from flask_mysqldb import MySQL
import sqlite3
import hashlib
from googletrans import Translator


import json
import time

app = Flask(__name__)

app.config['MYSQL_USER'] = "sql12614648"
app.config['MYSQL_PASSWORD'] = "1Sll3AXEpE"
app.config['MYSQL_HOST'] = "sql12.freemysqlhosting.net"
app.config['MYSQL_DB'] = "sql12614648"
app.config['MYSQL_CURSORCLASS'] = "DictCursor"

mysql = MySQL(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://sql12614648:1Sll3AXEpE@sql12.freemysqlhosting.net/sql12614648'

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://ssql12614648:sf1gti5Qpa@sql12.freemysqlhosting.net/sql12613760'


# mysql = MySQL(app)

# print(MySQL.connection, "Connection")

db = SQLAlchemy(app)

# Session = sessionmaker(bind=db.engine)

nirmal=[]

# with open('C:\\Users\\Nirmal Mina\\Desktop\\New\\home_zip\\static\\package_prod_det.json','r') as c:
#     params = json.load(c)["params"]


# @app.route('/prod')
# def index():
#     # Fetch data from the database
#     cur = db.connection.cursor()
#     cur.execute("SELECT * FROM tablename")
#     # cur.execute("SELECT * FROM tablename")
#     data = cur.fetchall()
#     cur.close()

#     # Render the template with the data
#     return render_template('prod_det.html', data=data)

class store(db.Model):
    id = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    or_price = db.Column(db.Integer, nullable=False)      
    discount = db.Column(db.String(5), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    about = db.Column(db.String(200), nullable=True)
    slug = db.Column(db.String(25), nullable=False)
    title = db.Column(db.String(25), nullable=True)
class perfume(db.Model):
    id = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    or_price = db.Column(db.Integer, nullable=False)      
    discount = db.Column(db.String(5), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    about = db.Column(db.String(200), nullable=True)
    slug = db.Column(db.String(25), nullable=False)
    title = db.Column(db.String(25), nullable=True)

class trimmer(db.Model):
    id = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    or_price = db.Column(db.Integer, nullable=False)      
    discount = db.Column(db.String(5), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    about = db.Column(db.String(200), nullable=True)
    slug = db.Column(db.String(25), nullable=False)
    title = db.Column(db.String(25), nullable=True)

class watches(db.Model):
    id = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    or_price = db.Column(db.Integer, nullable=False)      
    discount = db.Column(db.String(5), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    about = db.Column(db.String(200), nullable=True)
    slug = db.Column(db.String(25), nullable=False)
    title = db.Column(db.String(25), nullable=True)

class bracelet_chains(db.Model):
    id = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    or_price = db.Column(db.Integer, nullable=False)      
    discount = db.Column(db.String(5), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    about = db.Column(db.String(200), nullable=True)
    slug = db.Column(db.String(25), nullable=False)
    title = db.Column(db.String(25), nullable=True)

class facewash(db.Model):
    id = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    or_price = db.Column(db.Integer, nullable=False)      
    discount = db.Column(db.String(5), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    about = db.Column(db.String(200), nullable=True)
    slug = db.Column(db.String(25), nullable=False)
    title = db.Column(db.String(25), nullable=True)

class tshirts(db.Model):
    id = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    or_price = db.Column(db.Integer, nullable=False)      
    discount = db.Column(db.String(5), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    about = db.Column(db.String(200), nullable=True)
    slug = db.Column(db.String(25), nullable=False)
    title = db.Column(db.String(25), nullable=True)

class all_item(db.Model):
    id = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    or_price = db.Column(db.Integer, nullable=False)      
    discount = db.Column(db.String(5), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    about = db.Column(db.String(200), nullable=True)
    slug = db.Column(db.String(25), nullable=False)
    title = db.Column(db.String(25), nullable=True)
    
@app.route("/product_detail/<string:post_slug>", methods=['GET'])
def prod_det(post_slug):
    prod_det = all_item.query.filter_by(slug=post_slug).all()[0:1]
    return render_template('prod_det.html', users=prod_det, ram=nirmal[0])

@app.route("/product_detail/<string:post_slug>", methods=['GET'])
def prod_det1(post_slug):
    
    return render_template('prod_det.html', users=prod_det, ram=nirmal[0])


@app.route("/product/<string:post_slug>", methods=['GET'])
def produ(post_slug):
    prod = all_item.query.filter_by(slug=post_slug).all()[0:1]
    return render_template('product.html', products=prod, ram=nirmal[0])
# @app.route("/product_detail", methods=['GET'])
# # @app.route("/post/", methods=['GET'])
# def post_route(post_slug):
#     # users = items.query.all(slug=post_slug)
#     prod_det = items.filter_by(slug=post_slug).first()
#     return render_template('prod_det.html', users=prod_det)
@app.route('/get_text', methods=['POST'])
def get_text():
    text = request.json['text']
    return text
    print(text)

@app.route('/search', methods=['GET', 'POST'])
def search_item():
    # with app.app_context():
    #     Session = sessionmaker(bind=db.engine)
    #     session = Session()
    if request.method == 'POST':
        query = request.form['query']
        # query = request.form['query']

        
        product1 = all_item.query.filter(all_item.name.contains(query))
        product2 = all_item.query.filter(all_item.title.contains(query))
        product3 = all_item.query.filter(all_item.description.contains(query))
        product4 = all_item.query.filter(all_item.title.contains(query))
        final = product1.union(product2, product3).all()
        print([x.name for x in final])
        # session=Session()
        # list1=[]
        # results= session.query(store).filter(store.name.contains(query)).all()
        # for i in results:
        #     list1.append(i.name)

     
        return render_template('product.html',products1=final, n = len(final), ram=nirmal[0])
        # session.commit()
    return render_template('search.html')

     
    #     return render_template('product.html',products1=product1,products2=product2, products3=product3,products4=product4)
    #     # session.commit()
    # return render_template('search.html')
@app.route('/search', methods=['GET', 'POST'])
def search_item1():
    # with app.app_context():
    #     Session = sessionmaker(bind=db.engine)
    #     session = Session()
    if request.method == 'POST':
        query = request.form['query']
        # query = request.form['query']

        
        product1 = all_item.query.filter(all_item.name.contains(query)).all()
        product2 = all_item.query.filter(all_item.title.contains(query)).all()
        product3 = all_item.query.filter(all_item.description.contains(query)).all()
        product4 = all_item.query.filter(all_item.title.contains(query)).all()
        # session=Session()
        # list1=[]
        # results= session.query(store).filter(store.name.contains(query)).all()
        # for i in results:
        #     list1.append(i.name)

     
        return render_template('product.html',products1=product1,products2=product2, products3=product3,products4=product4, ram=nirmal[0])
        # session.commit()
    return render_template('product.html')




# @app.route('/produc', methods=['POST'])
# def search_item():
#     query = request.form['query']
#     cur = db.connection.cursor()
#     cur.execute("SELECT * FROM store WHERE name LIKE %s", ('%' + query + '%',))
#     results = cur.fetchall()
#     cur.close()
#     return render_template('product.html', products1=results)


# @app.route('/search/<search_query>')   
# def search_items(search_query):
#     items = store.query.filter(store.name.like('%'+search_query+'%')).all()
#     return render_template('search_results.html', items=items)

@app.route('/search_result', methods=['POST'])
def search_result():
    name = request.form.get("name")
    session=session()
    # text = request.json['text']
    # return text
    # print(text)
    list1=[]
    results= session.query(store).all()
    for i in results:
        if (name in i.name) is True:
            list1.append(i.name)
    return render_template("product.html",count=len(list1),result=list1, ram=nirmal[0])
    session.commit()


@app.route('/time')
def get_current_time():
    return {'time': time.time()}



@app.route("/")
def home():
    if len(request.cookies) > 0:
        username = request.cookies.get("username")
        
        token = request.cookies.get("token")
        cur = mysql.connection.cursor()
        cur.execute(f"SELECT * from users WHERE username='{username}'")
        results = cur.fetchall()
        if token == results[0]['password']:  
            nirmal.append(username)
            return render_template('homepage.html', data = {'username':username})
            # return render_template('men.html', data = {'username':username})
        else:
            # nirmal.append("login")
            return render_template('homepage.html')
    else:
        
        return render_template('homepage.html')

# print(username)
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
                 return render_template("login.html", feedback="Oops! Incorrect password")


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

        translator = Translator()
        detected_language = translator.detect(message).lang
        translation = translator.translate(message, src=detected_language, dest='en')

        cur.execute(f"INSERT INTO contactus (name, email, message) VALUES ('{name}', '{email}', '{translation.text}');")
        mysql.connection.commit()

        return render_template("contact.html", feedback="We've received your message")



@app.route("/homepage")
def homepage():
    
    return redirect("/")

@app.route("/men")
def men():
    nirmal.append("login")
    return render_template('men.html', ram=nirmal[0])

@app.route("/trends")
def trends():
    return render_template('trends.html', ram=nirmal[0])

@app.route("/collections")
def collections():
    return render_template('collections.html', ram=nirmal[0])

@app.route("/search")
def search(): 
    return render_template('search.html', ram=nirmal[0])

@app.route("/cart")
def cart():
    return render_template('cart.html', ram=nirmal[0])

@app.route("/product1")
def product1():
    
    prod1 = store.query.filter_by().all()[0:1]
    prod2 = store.query.filter_by().all()[0:3]
    prod3 = store.query.filter_by().all()[0:5]
    prod4 = store.query.filter_by().all()[0:7]
    return render_template('product.html',products1=prod1,products2=prod2,products3=prod3,products4=prod4, ram=nirmal[0])

@app.route("/product2")
def product2():
    
    prod1 = perfume.query.filter_by().all()[0:3]
    prod2 = perfume.query.filter_by().all()[0:1]
    prod3 = perfume.query.filter_by().all()[0:2]
    prod4 = perfume.query.filter_by().all()
    return render_template('product.html',products1=prod1,products2=prod2,products3=prod3,products4=prod4, ram=nirmal[0])

@app.route("/product3")
def product3():
    
    prod1 = trimmer.query.filter_by().all()[0:3]
    prod2 = trimmer.query.filter_by().all()[0:1]
    prod3 = trimmer.query.filter_by().all()[0:2]
    prod4 = trimmer.query.filter_by().all()
    return render_template('product.html',products1=prod1,products2=prod2,products3=prod3,products4=prod4, ram=nirmal[0])

@app.route("/product4")
def product4():
    
    prod1 = watches.query.filter_by().all()[0:3]
    prod2 = watches.query.filter_by().all()[0:1]
    prod3 = watches.query.filter_by().all()[0:2]
    prod4 = watches.query.filter_by().all()
    return render_template('product.html',products1=prod1,products2=prod2,products3=prod3,products4=prod4, ram=nirmal[0])

@app.route("/product5")
def product5():
    
    prod1 = bracelet_chains.query.filter_by().all()[0:3]
    prod2 = bracelet_chains.query.filter_by().all()[0:1]
    prod3 = bracelet_chains.query.filter_by().all()[0:2]
    prod4 = bracelet_chains.query.filter_by().all()
    return render_template('product.html',products1=prod1,products2=prod2,products3=prod3,products4=prod4, ram=nirmal[0])

@app.route("/product6")
def product6():
    
    prod1 = facewash.query.filter_by().all()[0:3]
    prod2 = facewash.query.filter_by().all()[0:1]
    prod3 = facewash.query.filter_by().all()[0:2]
    prod4 = facewash.query.filter_by().all()
    return render_template('product.html',products1=prod1,products2=prod2,products3=prod3,products4=prod4, ram=nirmal[0])

@app.route("/product7")
def product7():
    
    prod1 = tshirts.query.filter_by().all()[0:3]
    prod2 = tshirts.query.filter_by().all()[0:1]
    prod3 = tshirts.query.filter_by().all()[0:2]
    prod4 = tshirts.query.filter_by().all()
    return render_template('product.html',products1=prod1,products2=prod2,products3=prod3,products4=prod4, ram=nirmal[0])


@app.route("/sale")
def sale():
    return render_template('sale.html', ram=nirmal[0])

@app.route("/faq")
def faq():
    return render_template('faq.html', ram=nirmal[0])

# @app.route("/contact")
# def contact():
#     return render_template('contact.html')

# @app.route("/prod_det")
# def prod_det():
#     return render_template('prod_det.html')

@app.route("/payment")
def payment():
    return render_template('payment.html', ram=nirmal[0])

@app.route("/account")
def account():
    return render_template('account.html', ram=nirmal[0])

@app.route("/confirm")
def confirm():
    return render_template('confirm.html', ram=nirmal[0])

@app.route("/thnk_fr_cont")
def thnk_fr_cont():
    return render_template('thnk_fr_cont.html', ram=nirmal[0])

@app.route("/recover")
def recover():
    return render_template('recover.html', ram=nirmal[0])

# @app.route("/after_order")
# def after_order1():
#     return render_template('after_order.html', ram=nirmal[0])

@app.route("/after_order/<string:post_slug>", methods=['GET'])
def after_order2(post_slug):
    prod_det = store.query.filter_by(slug=post_slug).all()[0:1]
    return render_template('after_order.html',users=prod_det , ram=nirmal[0])

# @app.route("/plate('after_order.html', users=prod_det)

@app.route("/bazaar", methods = ["GET", "POST"])
def bazaar():
    cur = mysql.connection.cursor()
    if request.method == "GET":
        return render_template('bazaar.html')
    else:
        name = request.form.get("name")
        productname = request.form.get("productname")
        description = request.form.get("description")
        price = request.form.get("price")
        image = request.files["image"].read()
        cur.execute("INSERT INTO bazaar (name, productname, description, price, image) VALUES (%s, %s, %s, %s, %s)", (name, productname, description, price, image))
        mysql.connection.commit()
        return render_template("bazaar.html", feedback="Product uploaded successfully")  

@app.route("/after_order", methods = ["GET", "POST"])
def after_order():
    cur = mysql.connection.cursor()

    if request.method == "GET":
        return render_template('after_order.html')
    else:
        name = request.form.get("name")
        email = request.form.get("email")
        mobile = request.form.get("mobile")
        address = request.form.get("address")

        

        cur.execute(f"INSERT INTO orderdetails (name, email, mobile, address) VALUES ('{name}', '{email}', '{mobile}', '{address}');")
        mysql.connection.commit()

        return render_template("confirm.html", feedback="We've received your order")

app.run(debug=True, port=5000)
