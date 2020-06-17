def helperFunction(myLinkedList, current, previous) : # This function reverses the linked list recursively
	# Base case
	if current.next is None : 
		myLinkedList.head = current  
		current.next = previous 
		return 

	next = current.next
	current.next = previous 
	
	# Recursive case
	helperFunction(myLinkedList, next, current)  

def reverse(myLinkedList): 
	# Check if the head node of the linked list is null or not
	if myLinkedList.head is None: 
		return 
	
	# Call the helper function --> main recursive function
	helperFunction(myLinkedList, myLinkedList.head, None) 