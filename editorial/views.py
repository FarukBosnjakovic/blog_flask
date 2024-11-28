from flask import Flask, render_template, redirect, url_for
from flask import Blueprint

views = Blueprint('views', __name__)


@views.route('/')
@views.route('/home')
def home():
    return render_template('home.html')
