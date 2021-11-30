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

@views.route("/finderrors", Method=['GET','POST'])
def home():
    textfile = request.args['original']
    inputwords = split(textfile," ")
    dict = {}
    for i in inputwords:
        if i not in correct_spellings:
            if(i.__contains__('_')):
                entry = i.split('_')[0]
                dict[i] = functions.autocomplete(entry)
            else:
                spellbee = []
                edit = functions.edit_distance(i)
                trigram = functions.Jaccard_trigram(i)
                fourgram = functions.Jaccard_fourgram(i)
                spellbee.append(edit)
                spellbee.append(trigram)
                spellbee.append(fourgram)
                dict[i] = spellbee

    return render_template("index.html")
 
