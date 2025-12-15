from flask import Flask
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)
password = input("Enter your MySQL password: ")
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=password
)
cursor = connection.cursor()

@app.route("/createdb/<dbname>")
def route1(dbname):
    cursor.execute(f"create database {dbname}")
    return {"status":"done"}

@app.route("/deletedb/<dbname>")
def route2(dbname):
    cursor.execute(f"drop database {dbname}")
    return {"status":"done"}

@app.route("/showdbs")
def route3():
    cursor.execute(f"show databases")
    return {"data":cursor.fetchall()}

app.run(debug=True)
