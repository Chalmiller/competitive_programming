class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def reverse(head):
  prev = None
  while head:
    next = head.next
    head.next = prev
    prev = head
    head = next
  return prev


def is_palindromic_linked_list(head):
  slow = head
  fast = head

  while fast is not None and fast.next is not None:
    fast = fast.next.next
    slow = slow.next

  reversed_second_half = reverse(slow)

  while head is not None and reversed_second_half is not None:
    if head.next != reversed_second_half.next:
      return False
  return True

def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(2)

  print("Is palindrome: " + str(is_palindromic_linked_list(head)))

  head.next.next.next.next.next = Node(2)
  print("Is palindrome: " + str(is_palindromic_linked_list(head)))


main()