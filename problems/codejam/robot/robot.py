#!/ms/dist/python/PROJ/core/2.7.1/bin/python

import os

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
		
	def move(self):
		if self.pos < self.seq[0]:
			self.pos = self.pos + 1 
		elif self.pos > self.seq[0]:
			self.pos = self.pos - 1
	
	def can_push(self):
			return self.controller.get_turn(self.time)==self.name and self.seq[0]==self.pos
	
	def next(self):
		if len(self.seq)!=0:
			if self.can_push():
				self.seq.pop(0)
				self.controller.pushed_button(self.time)
			else:
				self.move()
		self.time+=1
		
	def complete(self):
		return len(self.seq)==0

def calculate_time(problem_string, bot_names):
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
	
	c = Controller(targets) 
	# a controller to check what the next taget is and if a button can be pressed
	orange = Robot(o,seq.get(o,[]), c)
	blue = Robot(b,seq.get(b,[]), c)

	#run the robots until there both complete
	while not(blue.complete()) or not(orange.complete()):
		orange.next()
		blue.next()

	return orange.time
	#they should always be the same and even if no orange sequence as the time still counts

def simplereadfile(filepath):
    with open(filepath, 'r') as f:
        return [line.rstrip(os.linesep) for line in f]

#run the over the file and output
problem_input=simplereadfile('/Users/mattalcock/Dev/tests/large.in')
problem_num=int(problem_input[0])
results = []

for p in problem_input[1::]:
	results.append(calculate_time(p, ("O","B")))

for i in xrange(len(results)):
	print "Case #%s: %s" % (i+1,results[i])
	

	

