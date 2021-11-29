from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify

views = Blueprint("views", __name__)


@views.route("/")
def index():
    return "hello-world"

@views.route("/home")
def home():
    return render_template("home.html")
