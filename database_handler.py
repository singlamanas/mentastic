from flask import Flask
from flask_mysqldb import MySQL

class DBHandler():
    
    def __init__(self, mysql):
        self.mysql = mysql
        print(mysql.connection)
        
    def initialize_database(self):
        cur = self.mysql.connection.cursor()
        cur.execute(f"CREATE TABLE users(id int IDENTITY(1,1) PRIMARYKEY, username VARCHAR(20), password VARCHAR(256))")
        self.mysql.connection.commit()

    def login_user(self, username, password):
        cur = self.mysql.connection.cursor()
        cur.execute(f"SELECT * from users WHERE username = '{username}'")
        results = cur.fetchall()
        if len(results) == 0:
            return (0, "Username does not exist")
        else:
            if password == results['password']:
                return (1, "User Found")
            else:
                return(0, "Incorrect Password")
