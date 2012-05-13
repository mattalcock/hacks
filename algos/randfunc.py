import random, string

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

#Produces a list of ints
def random_int_list(size=100, start=0, end=1000):
    return (random.randrange(start,end,1) for x in xrange(size))
    
    
if __name__ == '__main__':
    print random_string()                   #Q36NXHGFW0
    print random_int()                      #56
    print random_digits()                   #915292325494
    print [i for i in random_int_list()]    #[212, 436, 615, 160, 775, ....]