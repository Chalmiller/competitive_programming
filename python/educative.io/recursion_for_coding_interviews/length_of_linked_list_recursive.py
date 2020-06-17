def length(testVariable, head) :
	if head:
		return 1 + length(testVariable, head.next)
	else:
		return 0