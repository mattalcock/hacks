#!/ms/dist/python/PROJ/core/2.7.1/bin/python

import os

class Button:
	def __init__(self):
		self.can_push=True
			
	def get_push(self):
		return self.can_push
		
	def set_push(self, new_state):
		self.can_push=new_state

class Robot:
	def __init__(self, name, seq, button):
		self.name=name
		self.seq=seq
		self.time=0
		self.pos=1 #postions are 1 based
		self.complete=False
		self.button=button 
		self.command_list=[]
		
	def next(self):
		if len(self.seq)==0:
			self.complete = True #do nothing
			self.command_list.append("Complete at button %s" % (self.pos))
		else:
			if (self.button.get_push() and self.pos==self.seq[0]):
				p = self.seq.pop(0) #push the button!
				self.button.set_push(False) # no other robot can push
				self.command_list.append("Pushing button %s" % (self.pos))
				if len(self.seq)==0:
					self.complete = True #do nothing
			else:
				#move robot move!
				if self.pos < self.seq[0]:
					self.pos = self.pos + 1 
					self.command_list.append("Moving to %s" % (self.pos))
				elif self.pos > self.seq[0]:
					self.pos = self.pos - 1 
					self.command_list.append("Moving to %s" % (self.pos))
				else:
					self.command_list.append("Waiting to push at %s" % (self.pos))
				self.button.set_push(True)	# other robots can push	if I am moving		
		self.time+=1 # time has to increment 
	
	def iscomplete(self):
		return self.complete
		
def simplereadfile(filepath):
    with open(filepath, 'r') as f:
        return [line.rstrip(os.linesep) for line in f]

def shortest_time(problem_string, bot_names):
	(o, b) = bot_names #currently only works for two robots
	
	# process the problem input
	seq_list=problem_string.split(' ')
	length = seq_list.pop(0)

	seq={}	#create a dict of sequences
	
	#take two items out of the list at a time by spining into a tupple
	for bot, pos in zip(seq_list[::2], seq_list[1::2]):	
		seq.setdefault( bot , [] ).append(int(pos))

	button = Button() # a shared button lock
	orange = Robot(o,seq.get(o,[]), button)
	blue = Robot(b,seq.get(b,[]), button)

	#run the robots until there both complete
	while not(blue.complete) or not(orange.complete):
		orange.next()
		blue.next()

	print orange.command_list
	print blue.command_list
	
	print orange.time
	print blue.time
	return orange.time
	#they should always be the same and even if no orange sequence as the time still counts

#run the over the file and output
problem_input=simplereadfile('/Users/mattalcock/Dev/tests/small.in')
problem_num=int(problem_input[0])

results = []

for p in problem_input[1::]:
	results.append(shortest_time(p, ("O","B")))

for i in xrange(len(results)):
	print "Case #%s: %s" % (i+1,results[i])
	

	

