from re import split
from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
import functions

views = Blueprint("views", __name__)
import nltk
nltk.download('words')

from nltk.corpus import words
correct_spellings = words.words()

@views.route("/")
def index():
    return render_template("index.html", error = False)

@views.route("/finderrors", methods=['GET','POST'])
def home():
    textfile = request.args['original']
    mode = request.args['mode']

    inputwords = textfile.split()
    
    dict = {}
    for i in inputwords:
        if i not in ['.','?','!',',']:
            i = i.strip('.')
            i = i.strip('?')
            i = i.strip('!')
            i = i.strip(',')

            if i not in correct_spellings:
                print(i)
                if(i.__contains__('_')):
                    entry = i.split('_')[0]
                    print(functions.autocomplete(entry))
                    dict[i] = functions.autocomplete(entry)
                else:
                    spellbee = 'error'
                    if mode=='1':
                        spellbee = functions.edit_distance(i)
                    if mode =='2':
                        spellbee = functions.Jaccard_trigram(i)
                    if mode == '3':
                        spellbee = functions.Jaccard_fourgram(i)
                    print(spellbee)
                    dict[i] = spellbee

    for word, value in dict.items():
        textfile = textfile.replace(word,value)
    print(textfile)
    return render_template("index.html", inp = textfile)
 
