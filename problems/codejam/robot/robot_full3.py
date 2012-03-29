#!/ms/dist/python/PROJ/core/2.7.1/bin/python

import os

# The controler works for lots of robots
class Controller:
	def __init__(self, targets):
		self.targets = targets
		self.time_lock={}
	
	def pushed_button(self, time):
		self.targets.pop(0)
		self.time_lock[time]=True
		
	def get_turn(self, time):
		if self.time_lock.get(time, False):
			return None #nobody can go it's been time locked
		else:
			bot, pos = self.targets[0]
			return bot

class Robot:
	def __init__(self, name, seq, controller):
		self.name=name
		self.seq=seq
		self.time=0
		self.pos=1 #postions are 1 based
		self.controller=controller 
		self.command_list=[]
		
	def move(self):
		if self.pos < self.seq[0]:
			self.pos = self.pos + 1 
			self.command_list.append("Moving to: %s" % (self.pos))
		elif self.pos > self.seq[0]:
			self.pos = self.pos - 1
			self.command_list.append("Moving to: %s" % (self.pos))
		else:
			self.command_list.append("Waiting at: %s" % (self.pos))
	
	def can_push(self):
			return self.controller.get_turn(self.time)==self.name and self.seq[0]==self.pos
	
	def next(self):
		if len(self.seq)!=0:
			if self.can_push():
				self.seq.pop(0)
				self.controller.pushed_button(self.time)
				self.command_list.append("Pushing button: %s" % (self.pos))
			else:
				self.move()
		self.time+=1
		
	def complete(self):
		return len(self.seq)==0

def simplereadfile(filepath):
    with open(filepath, 'r') as f:
        return [line.rstrip(os.linesep) for line in f]

def shortest_time(problem_string, bot_names):
	(o, b) = bot_names #currently only works for two robots
	
	# process the problem input
	seq_list=problem_string.split(' ')
	length = seq_list.pop(0)

	seq={}	#create a dict of sequences
	targets=[]
	
	#take two items out of the list at a time by spining into a tupple
	for bot, pos in zip(seq_list[::2], seq_list[1::2]):	
		seq.setdefault( bot , [] ).append(int(pos))
		targets.append((bot,pos))
	
	#print targets
	
	c = Controller(targets) # a shared button lock
	orange = Robot(o,seq.get(o,[]), c)
	blue = Robot(b,seq.get(b,[]), c)

	#run the robots until there both complete

	while not(blue.complete()) or not(orange.complete()):
		orange.next()
		blue.next()
	
	#print orange.command_list
	#print blue.command_list
	
	#print orange.time
	#print blue.time
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
	

	

