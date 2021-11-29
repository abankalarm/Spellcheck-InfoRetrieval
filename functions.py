import nltk
# nltk.download('words')

from nltk.corpus import words
correct_spellings = words.words()

def edit_distance(entries):

    # get first letter of each word with c
    c = [i for i in correct_spellings if i[0]==entries[0]]
    # calculate the distance of each word with entry and link both together
    one = [(nltk.jaccard_distance(set(nltk.ngrams(entries, n=4)), \
                                  set(nltk.ngrams(a, n=4))), a) for a in c]
    output = sorted(one)[0][1]

    return output

print(edit_distance('ambulanc'))

def Jaccard_fourgram(entries):

    # get first letter of each word with c
    c = [i for i in correct_spellings if i[0]==entries[0]]
    # calculate the distance of each word with entry and link both together
    one = [((nltk.edit_distance(entries, a)), a) for a in c]

    # sort them to ascending order so shortest distance is on top.
    # extract the word only
    output = sorted(one)[0][1]

    return output

print(Jaccard_fourgram('ambulantce'))

def Jaccard_trigram(entries):
    # get first letter of each word with c
    c = [i for i in correct_spellings if i[0]==entries[0]]
    # calculate the distance of each word with entry and link both together
    one = [(nltk.jaccard_distance(set(nltk.ngrams(entries, n=3)), \
                                  set(nltk.ngrams(a, n=3))), a) for a in c]

    # sort them to ascending order so shortest distance is on top.
    # extract the word only
    output = sorted(one)[0][1]

    return output

print(Jaccard_trigram('ambulantce'))

def compare_full(orignal,tocompare):
    i = len(orignal)
    if(len(tocompare)<i):
        return False
    for x in range(0,i-1):
        if(orignal[x] != tocompare[x]):
            return False
    return True


def autocomplete(entries):
    # get first letter of each word with c
    c = [i for i in correct_spellings if compare_full(entries,i)==True]
    # calculate the distance of each word with entry and link both together
    one = [(nltk.jaccard_distance(set(nltk.ngrams(entries, n=3)), \
                                  set(nltk.ngrams(a, n=3))), a) for a in c]

    # sort them to ascending order so shortest distance is on top.
    # extract the word only
    output = sorted(one)[0][1]

    return output

print(autocomplete("eavesd"))