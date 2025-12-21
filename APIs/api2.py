from flask import Flask
from random import choice
import getpass
from flask_cors import CORS
import mysql.connector

flask1 = Flask(__name__)
passw1 = getpass.getpass("Enter your MySQL password: ")
print(passw1)
CORS(flask1)
mconn1 = mysql.connector.connect(
    host="localhost",
    user="root",
    database="JokeManagerDB",
    password=passw1
)
cursor1 = mconn1.cursor()

@flask1.route("/insertjoke/<joke>")
def route1(joke):
    cursor1.execute('insert into jokes (joke) values ' + '("' + joke + '");')
    return {"status":"success"}


@flask1.route("/fetchjoke/")
def route2():
    cursor1.execute("select * from jokes;")
    data1 = cursor1.fetchall()
    data2 = []
    for i in data1:
        data2.append(i[0])
    return {"status":"success", "response":choice(data2)}

flask1.run()
