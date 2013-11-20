import re, collections, sys

def words(text):
    return re.findall('[A-Za-z0-9\']+', text)

def match_names(text):
    return re.findall('[A-Z][a-z]*', text)

def paragraphs(text):
    return text.split('\r\n')

def sentences(text):
    return text.split('.')

def train(features, model=collections.defaultdict(lambda: 0)):
    for f in features:
        model[f] += 1
    return model


alphabet = 'abcdefghijklmnopqrstuvwxyz'
gender_pronouns = {'he':1, 'him':1, 'his':1, 'himself':1, 'she':-1, 'her':-1, 'herself':-1}
NAMES = train(match_names(file('../data/corpus.txt').read()))
#print NAMES.keys()

def score_text(text):
    score = 0
    for w in words(text):
        if w.lower() in gender_pronouns:
            score += gender_pronouns[w.lower()]
    return score

def score_snippets2(snippets):
    name_model = collections.defaultdict(lambda: [])
    #print paragrpahs
    for p in snippets:
        if p:
            names_found = set(match_names(p))
            score = score_text(p)
            if len(names_found)>2:
                for name in list(names_found):
                    name_model[name].append(score)
    return name_model

def score_snippets(snippets):
    name_model = collections.defaultdict(lambda: 0)
    #print paragrpahs
    for p in snippets:
        if p:
            names_found = set(match_names(p))
            score = score_text(p)
            for name in names_found:
                name_model[name]+=score
    return name_model

NAME_SENTENCE_SCORES = score_snippets2(sentences(file('../data/corpus.txt').read()))
NAME_PARA_SCORES = score_snippets(paragraphs(file('../data/corpus.txt').read()))
#print NAME_SCORES

def predict_gender(name):
    sent_scores = NAME_SENTENCE_SCORES.get(name, [])
    para_score = NAME_PARA_SCORES.get(name, 0)
    print name, sent_scores, para_score
    if para_score + sum(sent_scores) > 0:
        return 'Male'
    else:
        return 'Female'

if __name__ == "__main__":
    firstLine, count = True, 0
    for line in sys.stdin:
        if firstLine:
            count = line
            firstLine=False
        else:
            print predict_gender(line.rstrip('\n'))

"""
python gender_classifier.py < predict_sample.in
python gender_classifier.py < predict_sample_large.in
"""