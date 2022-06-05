from flask import Flask
from flask import render_template, url_for, redirect, request
import mysql.connector

app = Flask(__name__)
from app import views