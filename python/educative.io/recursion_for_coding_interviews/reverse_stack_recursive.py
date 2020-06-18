def insertAtBottom(stack, item) : # Recursive function that inserts an element at the bottom of a stack.
  # Base case
  if s.isEmpty(stack) :
    s.push(stack, item)

  # Recursive case
  else:
    temp = s.pop(stack)
    insertAtBottom(stack, item)
    s.push(stack, temp) 

def reverse(stack) :
  # Recursive case
  if not s.isEmpty(stack) :
    temp = s.pop(stack)
    reverse(stack)
    insertAtBottom(stack, temp) 