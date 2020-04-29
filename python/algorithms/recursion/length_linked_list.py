 import linkedList as l

def length(testVariable, head) :
	# Base case
	if (not head) :
		return 0
		
	# Recursive case
	else :
		return 1 + length(testVariable, head.next) 