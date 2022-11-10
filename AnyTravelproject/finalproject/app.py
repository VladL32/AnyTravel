import uvicorn as uvicorn
from flask import Flask, request, session, redirect, url_for, render_template, flash
from fastapi.middleware.wsgi import WSGIMiddleware

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.secret_key = 'VladLi.x_x'

UPLOAD_FOLDER = 'static/uploads/'

app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:////Users/a1231/Downloads/AnyTravelproject/finalproject/anytravel.db'


# from flask_sqlalchemy import SQLAlchemy
# from webpart.apps import db


class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True)  # integer primary key will be autoincremented by default
    login = db.Column(db.String(255), unique=True, nullable=False)
    user_fname = db.Column(db.String(255))
    number = db.Column(db.String(255))
    password = db.Column(db.String(255), nullable=False)

    # user_cars = db.relationship("Car", back_populates="owner", cascade="all, delete-orphan")

    user_reports = db.relationship("Reports", back_populates="report_all", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"User(user_id {self.user_id!r}, login={self.login!r},name={self.user_fname!r}, number={self.number!r})"


class Reports(db.Model):
    __tablename__ = "reports"
    report_id = db.Column(db.Integer, primary_key=True)  # integer primary key will be autoincremented by default
    login = db.Column(db.String(255), unique=True, nullable=False)
    user_fname = db.Column(db.String(255))
    number = db.Column(db.String(255))
    reason = db.Column(db.String(255))
    report = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)

    report_all = db.relationship("User", back_populates="user_reports")

    def __repr__(self) -> str:
        return f"Report(user_id={self.user_id_id!r},login={self.login!r},name={self.user_fname!r}, number={self.number!r}, reason={self.reason!r},report={self.report!r})"


class Tour(db.Model):
    __tablename__ = "tours"
    tour_id = db.Column(db.Integer, primary_key=True)  # integer primary key will be autoincremented by default
    date = db.Column(db.String(255))
    people_number = db.Column(db.Integer)
    tour_type = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)

    def __repr__(self) -> str:
        return f"User(user_id {self.user_id!r}, date={self.date!r},number={self.people_number!r}, number={self.tour_type!r})"


def add_user(user: User) -> None:
    db.session.add(user)
    db.session.commit()


def add_report(reports: Reports) -> None:
    db.session.add(reports)
    db.session.commit()


def add_tour(tours: Tour) -> None:
    db.session.add(tours)
    db.session.commit()


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


@app.route('/assignment')
def landing():
    return render_template('assignment.html')


@app.route('/reports', methods=["GET", "POST"])
def report():
    if request.method == "POST":
        login = request.form['email']
        fname = request.form['name']
        number = request.form['phone']
        reason = request.form['reason']
        report = request.form['report']
        add_report(
            Reports(login=login, user_fname=fname, number=number, reason=reason, report=report, user_id=session['uid']))
        return render_template('reports.html', context="Your complaint will be considered")
    return render_template('reports.html')


@app.route("/registr", methods=["GET", "POST"])
def registr(context=None):
    if request.method == "POST":
        login = request.form['email']
        fname = request.form['name']
        number = request.form['phone']
        pass1 = request.form['password']
        pass2 = request.form['form_retype_password']

        print(login, fname, number, pass1, pass2)

        data = db.session.query(User).filter_by(login=login).first()

        if data:
            return render_template("registr.html", context="The user with this login already exists!")
            # return redirect(url_for("register", error="Already registered!"))
        elif pass1 != pass2:
            return render_template("registr.html", context="Passwords do not match!")
            # return redirect(url_for("register", error="Passowords do not match!"))
        else:
            add_user(User(login=login, user_fname=fname,
                          number=number,
                          password=pass1))

        return redirect(url_for("login", context="Succesfully registered!"))

    return render_template("registr.html", context=context)


@app.route("/login", methods=["GET", "POST"])
def login(context=None):
    if request.method == "POST":

        user = db.session.query(User).filter_by(login=request.form['email'], password=request.form['password']).first()
        print(user)
        if user:
            session['authenticated'] = True
            session['uid'] = user.user_id
            session['username'] = user.user_fname
            return redirect(url_for("homepage", user_id=user.user_id))
        else:
            return render_template("login1.html", context="The login or password were wrong")

    return render_template("login1.html", context=context)


@app.route('/home/<int:user_id>', methods=["GET", "POST"])
def homepage(user_id):
    if request.method == "POST":
        date = request.form['datetour']
        number_people = request.form['num']
        name_of_tour = request.form['tour']
        add_tour(Tour(date=date, people_number=number_people, tour_type=name_of_tour, user_id=session['uid']))
        return render_template("home.html", ans="You were succesfully registered!")

    user_tours_query = db.session.query(Tour.date, Tour.people_number, Tour.tour_type).filter(
        Tour.user_id == user_id).first()
    query = db.session.query(User.login, User.user_fname, User.number).filter(User.user_id == user_id).first()
    if user_tours_query:
        return render_template('home.html', result=user_tours_query, context=query)
    if query:
        return render_template("home.html", context=query)
    else:
        query = db.session.query(User).filter(User.user_id == user_id).first()
        return render_template("home.html", context=query, result=None)


@app.route("/logout")
def logout():
    session.pop('authenticated', None)
    session.pop('uid', None)
    session.pop('username', None)
    return redirect(url_for('assignment'))


if __name__ == "__main__":
    with app.app_context():
        db.init_app(app)
        db.create_all()
        app.run(port=3221, debug=True)
