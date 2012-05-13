from operator import itemgetter
from array import array
from randfunc import random_int_list
####### Search Functions

#Tells you if somthing exists (True/False)
def binary_search_func(sortedlist, x):
    l = len(sortedlist)
    if l==1:
        if sortedlist[0]==x:
            return True
        else:
            return False
    else:
        cut=l/2
        if x == sortedlist[cut]:
            return True
        elif x> sortedlist[cut]:
            return binary_search_func(sortedlist[cut:], x)
        else:
            return binary_search_func(sortedlist[:cut], x)
            
#Tells you if somthing exists if it does you get it back otherwise -1 [while style]
def binary_search(sortedlist, x, lo=0, hi=None):
    if not hi:
        hi = len(sortedlist)
    while lo < hi:
        mid = (lo+hi)/2
        midval = sortedlist[mid]
        if midval<x:
            lo=mid+1
        elif midval>x:
            hi = mid
        else:
            return x
    return -1
    
#Tells you the location of somthing in a list otherwise -1 [while style]
def binary_find(sortedlist, x, lo=0, hi=None):
    if not hi:
        hi = len(sortedlist)
    while lo < hi:
        mid = (lo+hi)/2
        midval = sortedlist[mid]
        if midval<x:
            lo=mid+1
        elif midval>x:
            hi = mid
        else:
            return mid  #Note this is the only thing different from the above.
    return -1

####### String Comparison & Sorting
#Python can compare 2 words out of the box but we want to convert a string into an int for sorting.
# if "he" < "hea" -> True
# if "he" < "hef" -> True
# if "he" < "ha" -> False
# if "he" < "h" -> False

#The magic here is ord with is a 3 digit number for a character we times this by 1000 so we get a digit representing the word
def word_to_int(word):
    num = 0
    for i in xrange(len(word)):
        x = (1000**i)*ord(word[i])
        num+=x
    return num

####### Sorting Functions

#Python Inbuilt Sort
def python_sort(l):
    return sorted(l)
    
#Merge
def merge(left, right):
    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
    
def mergearrays(left, right):
    i, j, c= 0, 0, 0
    x = len(left) + len(right)
    result = array('l')
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    c+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

#Merge Sort
def merge_sort(l, mergef=merge):
    length = len(l)
    cut=length/2
    if length<=1:
        return l
    left = merge_sort(l[:cut])
    right = merge_sort(l[cut:])
    return list(mergef(left, right))
    
#Merge Sort
def merge_sort2(l, mergef=mergearrays):
    length = len(l)
    cut=length/2
    if length<=1:
        return l
    left = merge_sort(l[:cut])
    right = merge_sort(l[cut:])
    return list(mergef(left, right))

#Quick Sort
def quick_sort(l):
    length = len(l)
    if length <=1:
        return l
    else:
        pivot = l.pop(int(length/2))
        less, more = [], []
        for x in l:
            if x<=pivot:
                less.append(x)
            else:
                more.append(x)
        return quick_sort(less) + [pivot] + quick_sort(more)

#Insertion Sort
def insert_sort(l):
    for i in range(1, len(l)):
        save=l[i]
        j=i
        while j>0 and l[j-1] > save:
            l[j] = l[j-1]
            j-=1
        l[j] = save
    return l

####### Adaptive Sorting Algos
def adapt_quick_sort(l, sortf=insert_sort, size=5):
    length = len(l)
    if length <= size:
        return sortf(l)
    else:
        pivot = l.pop(int(length/2))
        less, more = [], []
        for x in l:
            if x<=pivot:
                less.append(x)
            else:
                more.append(x)
        return quick_sort(less) + [pivot] + quick_sort(more)

def adapt_merge_sort(l, sortf=insert_sort, size=7):
    length = len(l)
    cut=length/2
    if length<=size:
        return insert_sort(l)
    left = merge_sort(l[:cut])
    right = merge_sort(l[cut:])
    return merge(left, right)

####### Hash Tables

if __name__ == '__main__':
    print [i for i in random_int_list()]    #[212, 436, 615, 160, 775, ....]
    
    #Binary Search - Functional Style
    print binary_search_func(range(100), 11)                         #True
    random_list = [i for i in random_int_list()]
    print binary_search_func(sorted(random_list), 12345)             #False (out of bounds)
    print binary_search_func(sorted(random_list), 333)               #True/Flase (1 in 10 chance)
    print binary_search_func(sorted(random_list), 567)               #True/Flase (1 in 10 chance)
    print binary_search_func(sorted(random_list), random_list[35])   #True as we picked from the input list
    
    #Binary Search - Inplace Style
    print binary_search(range(100), 11)                         #11
    print binary_search(sorted(random_list), 12345)             #-1 (out of bounds)
    print binary_search(sorted(random_list), 333)               #-1 or 333 (1 in 10 chance)
    print binary_search(sorted(random_list), 567)               #-1 or 567 (1 in 10 chance)
    print binary_search(sorted(random_list), random_list[35])   #Value of location 35 (When I ran it was 552)
    
    #Binary Find
    print binary_find(sorted(random_list), sorted(random_list)[35]) #35 The location of item 35 should be 35
    
    #String Sorting
    words = ["hello", "hella", "aello", "hallo"]
    print words
    print sorted(words)
    meta = [(i,word_to_int(words[i]), words[i]) for i in xrange(len(words))]
    print meta
    print sorted(meta, key=itemgetter(1))
    
    #Sorting
    random_list = [i for i in random_int_list(6)]
    print merge_sort(random_list)
    
    random_list = [i for i in random_int_list()]
    print merge_sort(random_list)
    
    random_list = [i for i in random_int_list()]
    print quick_sort(random_list)
    
    random_list = [i for i in random_int_list()]
    print insert_sort(random_list)
    
    random_list = [i for i in random_int_list()]
    print merge_sort(random_list, mergef=mergearrays)
    
    #Speed Tests
    

