from ..linked_list import LinkedListNode

def delete_node(head, key):
  """
  1. Prev will be set to a sentinel node at first
  2. Iterate through the linked_list - O(n) worst case
  3. If the curr value is the key to delete, prev.next should be set to curr.next
  4. Return head since it's memory address reference should not be changed

  Edge Case:
    - If the node to delete is the first node or the linked list is empty

  Time Complexity = O(n)
  Space_Complexity = O(1) constant because only one sentinel node is created
  """
  if not head:
    return head

  prev = None
  curr = head

  while curr:
    if curr.data is key:
      if curr is head:
        head = head.next
      else:
        prev.next = curr.next
        curr = curr.next
    else:
      prev = curr
      curr = curr.next

  return head