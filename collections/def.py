from collections import defaultdict

def run():

    data = [('a', 'x', 2), ('a', 'y', 1), ('a', 'z', 3),('b', 'x', 0),
         ('b', 'y', 5),('b', 'z', 2), ('c', 'x', 2), ('c', 'z', 2)]


    ocounter = {}
    for d1, d2, m in data:
        print d1,d2,m
        try:
            inner = ocounter[d1]
            inner.update({d2: inner.get(d2, 0) + m })
        except KeyError as e:
            inner = {d2:m}
        ocounter[d1]=inner
    print ocounter


    counter = defaultdict(lambda: defaultdict(lambda: 0))
    for d1, d2, m in data:
        print d1,d2,m
        counter[d1][d2]+=m
    print counter


if __name__ == '__main__':
    
    run()