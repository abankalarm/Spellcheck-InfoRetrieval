
import functions
from re import split
import nltk
# nltk.download('words')

from nltk.corpus import words
correct_spellings = words.words()

def home():
    textfile = "helllo, I thouggt you could use some medici_, do you need help? you loook injuread"
    mode = 2
    inputwords = textfile.split()
    print(inputwords)
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
                    if mode==1:
                        spellbee = functions.edit_distance(i)
                    if mode ==2:
                        spellbee = functions.Jaccard_trigram(i)
                    if mode == 3:
                        spellbee = functions.Jaccard_fourgram(i)
                    print(spellbee)
                    dict[i] = spellbee

    for word, value in dict.items():
        textfile = textfile.replace(word,value)

    print(textfile)
 
home()
