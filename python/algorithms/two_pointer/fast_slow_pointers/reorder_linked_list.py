from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(str(temp.value) + " ", end='')
      temp = temp.next
    print()


def reorder(head):
  slow, fast = head, head
  while fast and fast.next:
    fast = fast.next.next
    slow = slow.next

  reverse_second_half = reverse(slow)
  head_first_half = head

  while head_first_half is not None and reverse_second_half is not None:
    temp = head_first_half.next
    head_first_half.next = reverse_second_half
    head_first_half = temp

    temp = reverse_second_half.next
    reverse_second_half.next = head_first_half
    reverse_second_half = temp

  if head_first_half is not None:
    head_first_half.next = None

def reverse(head):
  prev  = None
  while head:
    next = head.next
    head.next = prev
    prev = head
    head = next
  return prev

def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(8)
  head.next.next.next.next = Node(10)
  head.next.next.next.next.next = Node(12)
  reorder(head)
  head.print_list()


main()