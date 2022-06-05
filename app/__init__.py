# la aplicacion de flask se encuentra aqui
#en este lugar iran las configuraciones

from flask import Flask
from flask import render_template, url_for, redirect, request


app = Flask(__name__)
from app import views