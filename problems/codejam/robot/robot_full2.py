#!/ms/dist/python/PROJ/core/2.7.1/bin/python

import os

# The controler works for lots of robots
class Controler:
	def __init__(self, robot_list):
		self.robot_dict = dict((r, False) for r in robot_list)
		self.turn=robot_list[0]
	
	def change_turn(self):
		for robot, done in self.robot_dict.iteritems():
			if done==False and self.turn!=robot:
				self.turn=robot
				break
				#print "changing turn to %s" % (robot)
	
	def complete(self, name):
		self.robot_dict[name]=True
			
	def my_turn(self, name):
		return self.turn==name
		

class Robot:
	def __init__(self, name, seq, controler):
		self.name=name
		self.seq=seq
		self.time=0
		self.pos=1 #postions are 1 based
		self.complete=False
		self.controler=controler 
		self.command_list=[]
		
	def next(self):
		if len(self.seq)==0:
			self.allcomplete() #do nothing
			command="Complete at button %s" % (self.pos)
			self.controler.change_turn()
		else:
			if (self.controler.my_turn(self.name) and self.pos==self.seq[0]):
				p = self.seq.pop(0) #push the button!
				command="Pushing button %s" % (self.pos)
				if len(self.seq)==0: self.allcomplete()
				self.controler.change_turn() # no other robot can push
			else:
				#move robot move!
				if self.pos < self.seq[0]:
					self.pos = self.pos + 1 
					command="Moving to %s" % (self.pos)
				elif self.pos > self.seq[0]:
					self.pos = self.pos - 1 
					command="Moving to %s" % (self.pos)
				else:
					command="Waiting to push at %s" % (self.pos)		
		self.time+=1 # time has to increment 
		#print command
		self.command_list.append(command)
	
	def iscomplete(self):
		return self.complete
	
	def allcomplete(self):
		self.complete=True
		self.controler.complete(self.name)
		
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

	controler = Controler([o,b]) # a shared button lock
	orange = Robot(o,seq.get(o,[]), controler)
	blue = Robot(b,seq.get(b,[]), controler)

	#run the robots until there both complete
	while not(blue.complete) or not(orange.complete):
		blue.next()
		orange.next()

	print orange.command_list
	print blue.command_list
	
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
	

	

