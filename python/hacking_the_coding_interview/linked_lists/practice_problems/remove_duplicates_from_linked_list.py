def remove_duplicates(head):
  """
  1. Iterate through the linked list and count up for each node
  2. If the count is already 1, link the previous head to the next
  3. I'll need to keep track of both the previous and current node
  4. Return the head since that address reference will not change during iteration

  Edge cases:
    - If the linked list is empty or has one node

  Time Complexity - O(n)
  Space Complexity - O(n) since we are just keeping a counter
  """
  # if not head:
  #   return head

  # node_count = {}
  # prev = None
  # curr = head

  # while curr:
  #   node_count[curr.data] = node_count.get(curr.data, 0) + 1
  #   next = curr.next
  #   if node_count[curr.data] > 1:
  #     prev.next = next
  #   prev = curr
  #   curr = next
  
  # return head

  """
  To solve in constant space
  """

  if head == None:
    return head

  dup_set = set()
  dup_set.add(head.data)
  curr = head

  while curr.next != None:
    if curr.next.data in dup_set:
      # Duplicate node found. Let's remove it from the list.
      curr.next = curr.next.next
    else:
      # Element not found in map, let's add it.
      dup_set.add(curr.next.data)
      curr = curr.next

  return head
