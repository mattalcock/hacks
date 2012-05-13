import time
from algos import merge_sort, python_sort, quick_sort, insert_sort, adapt_quick_sort, adapt_merge_sort, merge_sort2§
from randfunc import random_int_list
from goochart import linechart

""" 
Speed test funciton
Given a function a list of list sizes to work on and a number of iterations
Return a list of tuples giving an average compute time of the function of each item in the list

 """

def speedtest(f, iterations=10, sizelist=[x*100 for x in xrange(1,10)], listgen=random_int_list):
    test_count, total_time = 0, 0
    time_results = []
    for s in sizelist:
        for i in xrange(iterations):
            test_list = list(listgen(s))
            start = time.time()
            r = f(test_list)
            duration =  (time.time() - start) * 1000
            #print "Function %s took %s on a list size of %s" % (f,s,duration)
            total_time +=duration
            test_count+=1
        time_results.append((s,total_time, test_count, total_time/test_count))
        test_count, total_time = 0, 0
    return time_results

if __name__ == '__main__':
    print "Basic 1,000 Items - Small"
    sizelist = [x*100 for x in xrange(1,10)]
    dataset=[]
    dataset.append(('Inbuilt', [(size, avg) for (size, t, c, avg) in speedtest(python_sort, sizelist=sizelist)]))
    print "Python Sort Done"
    dataset.append(('Merge',[(size, avg) for (size, t, c, avg) in speedtest(merge_sort, sizelist=sizelist)]))
    print "Merge Sort Done"
    dataset.append(('Quick',[(size, avg) for (size, t, c, avg) in speedtest(quick_sort, sizelist=sizelist)]))
    print "Quick Sort Done"
    dataset.append(('Insert',[(size, avg) for (size, t, c, avg) in speedtest(insert_sort, sizelist=sizelist)]))
    print "Insert Sort Done"
    linechart('sort-compare-small.png', dataset)
    
    print "Basic 50 Items - Micro"
    sizelist = [x*2 for x in xrange(1,25)]
    dataset=[]
    dataset.append(('Inbuilt', [(size, avg) for (size, t, c, avg) in speedtest(python_sort, sizelist=sizelist)]))
    print "Python Sort Done"
    dataset.append(('Merge',[(size, avg) for (size, t, c, avg) in speedtest(merge_sort, sizelist=sizelist)]))
    print "Merge Sort Done"
    dataset.append(('Quick',[(size, avg) for (size, t, c, avg) in speedtest(quick_sort, sizelist=sizelist)]))
    print "Quick Sort Done"
    dataset.append(('Insert',[(size, avg) for (size, t, c, avg) in speedtest(insert_sort, sizelist=sizelist)]))
    print "Insert Sort Done"
    linechart('sort-compare-micro.png', dataset)
    
    print "Basic 50 Items "
    sizelist = [x*1000 for x in xrange(1,10)]
    dataset=[]
    dataset.append(('Inbuilt', [(size, avg) for (size, t, c, avg) in speedtest(python_sort, sizelist=sizelist)]))
    print "Python Sort Done"
    dataset.append(('Merge',[(size, avg) for (size, t, c, avg) in speedtest(merge_sort, sizelist=sizelist)]))
    print "Merge Sort Done"
    dataset.append(('Quick',[(size, avg) for (size, t, c, avg) in speedtest(quick_sort, sizelist=sizelist)]))
    print "Quick Sort Done"
    dataset.append(('Adapt Quick - 7',[(size, avg) for (size, t, c, avg) in speedtest(adapt_quick_sort, sizelist=sizelist)]))
    print "Adapt Quick - 5 Sort Done"
    dataset.append(('Adapt Merge - 7',[(size, avg) for (size, t, c, avg) in speedtest(adapt_merge_sort, sizelist=sizelist)]))
    print "Adapt Merge - 5 Sort Done"
    dataset.append(('Merge 2',[(size, avg) for (size, t, c, avg) in speedtest(merge_sort2, sizelist=sizelist)]))
    print "Merge 2 -  Sort Done"
    linechart('sort-compare.png', dataset)
    