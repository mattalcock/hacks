#!/ms/dist/python/PROJ/core/2.7.1/bin/python

import os

def process_base(base, recipe):
	base = list(base)
	r=base.pop()
	changed=False
	#print recipe
	for i in xrange(len(recipe)-1):
		check=recipe[i:i+2]
		#print "checking %s with %s" % (check, base)
		if check==base:
			#print "replacing %s with %s" % (check, r)
			recipe[i:i+2] = r
			changed=True
	if not(changed):
		for i in xrange(len(recipe)-1):
			check=recipe[i:i+2]
			#print "checking %s with %s" % (check, base)
			if check==base[::-1]:
				#print "replacing %s with %s" % (check, r)
				recipe[i:i+2] = r
				changed=True	
	return recipe

def list_find(L, value):
	try:
		i = L.index(value)
	except ValueError:
		i = -1 # no match
	return i

def process_oppose(oppose, recipe):
	a=oppose[0]
	b=oppose[1]
	for i in xrange(len(recipe)):
		if recipe[i]==a:
			x=list_find(recipe[i::],b)
			if x!=-1:
			    #print "deleting %s between %s" % (i,x+1)
			    del recipe[i:x+1]
			    return recipe
		if recipe[i]==b:
			x=list_find(recipe[i::],a)
			if x!=-1:
			    #print "deleting %s between %s" % (i,x+1)
			    del recipe[i:x+1]
			    return recipe
	return recipe

def process_list(line):
	line_list=line.split(' ')
	#print line_list
	
	c=int(line_list.pop(0))
	base_list=[]
	for i in xrange(c):
		base_list.append(line_list.pop(i))
	
	d=int(line_list.pop(0))
	oppose_list=[]
	for i in xrange(d):
		oppose_list.append(line_list.pop(i))
		
	n=int(line_list.pop(0))
	recipe=list(line_list.pop(0))
	
	for o in oppose_list:
		recipe = process_oppose(o, recipe)
	
	#print recipe
	
	for b in base_list:
		recipe = process_base(b, recipe)
	
	#print recipe
	return recipe
	

def simplereadfile(filepath):
    with open(filepath, 'r') as f:
        return [line.rstrip(os.linesep) for line in f]

#run the over the file and output
problem_input=simplereadfile('/Users/mattalcock/Dev/tests/codejam/magicka/small.in')
problem_num=int(problem_input[0])
results = []

for p in problem_input[1::]:
	results.append(process_list(p))

for i in xrange(len(results)):
	print "Case #%s: %s" % (i+1,str(results[i]).replace('\'',''))
	

	

