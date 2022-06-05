from flask import Flask
from flask import render_template, url_for, redirect, request
import mysql.connector


database = mysql.connector.connect(
    host="127.0.0.1",
  user="root",
  password="Fadryel#14",
  database="BlogtosDb"
)

cursor = database.cursor()

cursor.execute("SHOW DATABASES")

for x in cursor:
    print(x)

print(database)

app = Flask(__name__)


@app.route("/",methods=["GET","POST"])
def loginPage():

    if request.method == "POST":
        userName = request.form.get("username")
        password = request.form.get("password")
        rememberCheckBox = request.form.get("checkbox")
        print(userName)
        print(password)
        print(rememberCheckBox)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)