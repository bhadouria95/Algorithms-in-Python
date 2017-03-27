#This program finds the no, of moves required to complete tower of hanoi problem

counter = 0

def moveTower(height, fromPole, toPole, withPole):
	if height >= 1:
		moveTower(height - 1, fromPole, withPole, toPole)
		moveDisks(fromPole, toPole)
		moveTower(height - 1, withPole, toPole, fromPole)

def moveDisks(fp, tp):
	counter += 1
	print("Moving disk from",fp,"to",tp)

moveTower(7,"A","B","C")
print(counter)