def reverse(head):
  """
  1. keep track of previous element and current element
  2. while curr.next exists, flip the next pointer to prev
  3. return prev, as that will be the new head
  """

  prev = None
  curr = head

  while curr:
    next = curr.next
    curr.next = prev
    prev = curr
    curr = next

  return prev