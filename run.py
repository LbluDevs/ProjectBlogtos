from app import app

#Enciende el servidor the flask, y nos permite testear la pagina (shift+ click derecho en el ip/port que da en consola y abre tu navegador)
if __name__ == "__main__":
    app.run(debug=True)