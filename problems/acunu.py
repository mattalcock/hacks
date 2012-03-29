#!/ms/dist/python/PROJ/core/2.7.1/bin/python
from collections import defaultdict

def hex_bitcount ( S ):
    hex_string="0x" + S.lower()
    n = int(hex_string,0)
    b = str(bin(n))[2::]
    total = sum(int(d)for d in b)
	#the above could all be done in one line if really required.
    return total
	

print hex_bitcount("2F")

def heavy_decimal_count ( A,B ):
    limit = 7
    heavy_count = 0
    for n in xrange(A, B+1):
       total = sum(int(d) for d in str(n))
       av = (total * 1.0) / len(str(n))
       if av > limit:
           heavy_count = heavy_count +1
    return heavy_count

print heavy_decimal_count(8675, 8689)

def arrLeader ( A ):
    counter = defaultdict(int)
    for a in A:
        counter[a]+=1
        
    s = sorted(counter.iteritems(), key=itemgetter(1), reverse=True)
    leader, count = s[0]
    
    if  count > (len(A))/2:
        return leader
    else:
        return -1
        
def arrLeader ( A ):
    lead_return = -1
    lead_count=0
    lead=A[0]
	
	#initalise a counter dictionary
    counter={}
    for i in A:
       try:
           c = counter[i]
           counter[i]=c+1
       except KeyError:
           counter[i]=1
    
    for k,v in counter.items():
		if v > lead_count:
			lead_count = v
			lead = k
    print "lead: %s" % (lead)		
    for k,v in counter.items():
       print "key: %s" % (k)
       print v
    if lead_count > (len(A))/2:
        lead_return = lead 
    return lead_return

listOne = [4,2,2,3,2,4,2,2,6,4]
listTwo = [100,50,1,1,1]
print arrLeader(listOne)
print arrLeader(listTwo)