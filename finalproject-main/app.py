import os.path
import re
from msilib.schema import File
import psycopg2
import psycopg2.extras
import uvicorn as uvicorn
from flask import Flask, request, session, redirect, url_for, render_template, flash
from fastapi.middleware.wsgi import WSGIMiddleware
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates



app = Flask(__name__)
app.secret_key = 'VladLi.x_x'

DB_HOST = "localhost"
DB_NAME = "users"
DB_USER = "VladLix_x"
DB_PASS = "12345678"

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

UPLOAD_FOLDER = 'static/uploads/'

app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

fapp = FastAPI()

fapp.mount('/', WSGIMiddleware(app))

templates = Jinja2Templates(directory="templates")

@app.route('/')
def assignment():
    return render_template('assignment.html')

@app.route('/aboutus')
def about():
    return render_template('aboutus.html')

@app.route('/contacts')
def contact():
    return render_template('contacts.html')

@app.route('/reports')
def report():
    return render_template('reports.html')

@app.route('/assignment')
def landing():
    return render_template('assignment.html')



if __name__ == "__main__":
    uvicorn.run(fapp, host='localhost', port=8000)