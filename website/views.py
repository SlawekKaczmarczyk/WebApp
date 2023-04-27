from flask import Blueprint, render_template

#Blueprint is for collecting routes and urls

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")