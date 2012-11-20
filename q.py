

if __name__ == '__main__':

    dave = [{'date':'12/10/12','time':'09:12','created_by':'adam','text':'this'},
            {'date':'28/09/11','time':'15:58','created_by':'admin','text':'that'},
            {'date':'28/09/11','time':'15:59','text':'those'},
            {'date':'03/01/10','time':'12:34','created_by':'admin','text':'this and that'}]

    ds = list(set(x['created_by'] for x in dave if 'created_by' in x))
    print ds