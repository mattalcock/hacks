import re, collections, sys

def lines(text):
    return text.split('\n')

def train(traning_tuples):
    model = collections.defaultdict(lambda: 0)

    for A, B, label in traning_tuples:
        winner = A if label==2 else B
        for c in winner:
            model[c]+=1

    return model

def get_teams(lines, team_size=5):
    for l in lines:
        broken = l.split(',')
        yield (broken[:team_size], broken[team_size:-1], broken[-1])

def predict_winner(name, model, team_size=5):
    broken = line.split(',')
    A, B = broken[:team_size], broken[team_size:-1]
    a = sum(model[i] for i in A)
    b = sum(model[i] for i in B)
    print a, b
    if a > b:
        return 1
    else:
        return 2

if __name__ == "__main__":

    WIN_MODEL = train(get_teams(lines(file('trainingdata.txt').read())))
    print WIN_MODEL

    firstLine, count = True, 0
    for line in sys.stdin:
        if firstLine:
            count = line
            firstLine=False
        else:
            predict =  predict_winner(line, WIN_MODEL)
            print predict

"""
python predict_basic.py < predict_sample.in
"""