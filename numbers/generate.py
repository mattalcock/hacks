import random, string
from operator import itemgetter

#######  Some functions to generate random things  ######

#Produces a random string, takes a seed list of chars
#Q36NXHGFW0
def random_string(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in xrange(size))

#Produces a random int between a range
#56
def random_int(start=0, end=100):
    return random.randrange(start,end,1)

#Produces a random digit or a fixed size of intergers
#915292325494
def random_digits(size=12):
    start=(10**(size-1))
    end=(10**(size))-1
    return random.randrange(start,end,1)

####### Random list functions

#Produces a random string, takes a sead list of char
def random_int_list(size=100, start=0, end=1000):
    return (random.randrange(start,end,1) for x in xrange(size))


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

#Merge Sort

#Quick Sort

####### Hash Tables

if __name__ == '__main__':
    print random_string()                   #Q36NXHGFW0
    print random_int()                      #56
    print random_digits()                   #915292325494
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
    
    #Speed Tests
    

