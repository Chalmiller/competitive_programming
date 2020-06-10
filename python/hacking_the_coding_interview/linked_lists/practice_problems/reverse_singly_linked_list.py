def reverse(head):
  """
  1. keep track of previous element and current element
  2. while curr.next exists, flip the next pointer to prev
  3. return prev, as that will be the new head

  complexity - O(n)
  space = O(1) - constant
  """

  # prev = None
  # curr = head

  # while curr:
  #   next = curr.next
  #   curr.next = prev
  #   prev = curr
  #   curr = next

  # return prev

  """
  There is also a recursive way to do this
  """
  if not head or not head.next:
    return head
  
  reverse_list = reverse(head.next)

  head.next.next = head
  head.next = None
  return reverse_list