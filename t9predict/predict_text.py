import re, collections, sys
from itertools import product

def words(text):
    return re.findall('[A-Za-z0-9\']+', text.lower())

def train(features, model=collections.defaultdict(lambda: 0), check=False):
    for f in features:
        if not check or f in model:
            model[f] += 1
    return model

def build_pregram(words):
    model = collections.defaultdict(lambda: [])
    for word in words:
        for i in xrange(1,len(word)):
            model[word[:i]].append(word)
    return model

DICTIONARY = train(words(file('t9Dictionary').read()))
NGRAMS = train(words(file('t9TextCorpus').read()), model=DICTIONARY, check=True)
PREGRAM = build_pregram(NGRAMS.keys())

alphabet = 'abcdefghijklmnopqrstuvwxyz'
button_config = {2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}

def gen_string_eqiv(numbers):
    try:
        combinations = [tuple(button_config[int(i)]) for i in numbers]
        return ["".join(combi) for combi in product(*combinations)]
    except KeyError as e:
        return []

def predict_text(numbers):
    words = gen_string_eqiv(numbers)
    guesses = [PREGRAM[w] for w in words if PREGRAM[w]]
    flattern_guesses = [item for sublist in guesses for item in sublist]
    candidates = [(w, NGRAMS[w]) for w in flattern_guesses if  NGRAMS[w]>0]
    candidates.extend([(w, NGRAMS[w]) for w in words if  NGRAMS[w]>0])
    first_sort = sorted(candidates, key=lambda x: x[0])
    top = sorted(first_sort, key=lambda x: x[1], reverse=True)[:5]

    if top:
        return ";".join([word for word, score in top])
    else:
        return 'No Suggestions'

if __name__ == "__main__":
    firstLine, count = True, 0
    for line in sys.stdin:
        if firstLine:
            count = line
            firstLine=False
        else:
            print predict_text(line.rstrip('\n'))

"""
python predict_text.py < t9predict_sample.in
"""