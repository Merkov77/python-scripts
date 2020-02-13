#-*- encoding:utf-8 -*-
#Botnet Tesla
import time, random

var, timer, address = False, 0.1, "190.200.31.185"
def syncall():
	lett, cons = ["a","e","i","o","u"], ["b","c","d","f","S","z","x","k","v","w","y","r"]
	name_bot = random.choice(lett) + random.choice(cons) + random.choice(lett) + random.choice(cons) + random.choice([random.choice(lett), random.choice(cons)]) + random.choice(lett)
	
	x, y, z, q = random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(80,160)
	function = (str(x)+"."+str(y)+"."+str(z)+"."+str(q))
	return "[ " + function + ":PORT - Bot-" + name_bot.capitalize() 

#print "Proceso:",self.x, "/ Velocity: +"+str(timer), syncall
class biprocess_net:
	def __init__(self, ref=9):
		self.ref = ref
	def p1(self):
		global var, timer
		print "Operating block A... \n"
	
		for self.x in range(self.ref+1):
			time.sleep(0.9-timer)
			print syncall(), "Sending package to " + address + "... ]"
			if self.x == self.ref:
				print "\n"
				var = True
				print  "Slowing the speed of block B...\n"

	def p2(self):
		global var, timer
		print "Operating block B... \n"
		
		for self.x in range(self.ref+1):
			time.sleep(0.1+timer)
			print syncall(), "Waiting... ]"
			if self.x == self.ref:
				print "\n"
				var = False
				print "Increasing speed of block A...\n"

object = biprocess_net()
while True:
	if var == False:
		object.p1()
	if var == True:
		object.p2()
	if timer > 0.8:
		timer = 0.0
		print "Balancing Speeds...\n"
	if timer < 0.8:
		timer += 0.1
	
