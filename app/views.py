"""
Todas las rutas HTML, estaran colocadas aqui, exepto por las rutas de admin
"""


from app import app
from app import url_for, render_template, request, redirect

@app.route("/",methods=["GET","POST"])
def loginPage():

    if request.method == "POST":
        userName = request.form.get("username")
        password = request.form.get("password")
        rememberCheckBox = request.form.get("checkbox")
        print(userName)
        print(password)
        print(rememberCheckBox)

        return redirect(url_for("homePage"))

    return render_template("public/index.html")


@app.route("/Home")
def homePage():

    return render_template("public/menu.html")
