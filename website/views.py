from re import split
from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
import functions

views = Blueprint("views", __name__)
import nltk
# nltk.download('words')

from nltk.corpus import words
correct_spellings = words.words()

@views.route("/")
def index():
    return render_template("index.html", error = False)

@views.route("/finderrors", Method=['POST'])
def home():
    textfile = request.args['original']
    inputwords = split(textfile)
    for i in inputwords:
        if i not in correct_spellings:
            print("x")
    return render_template("index.html")
 
