from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()


def rotate(head, rotations):
    
    if head is None or head.next is None or rotations <= 0:
        return head
    last_node = head
    list_length = 1
    while last_node.next is not None:
        last_node = last_node.next
        list_length += 1
    
    last_node.next = head
    rotations %= list_length
    skip_length = list_length - rotations
    last_node_of_roatated = head
    for i in range(skip_length - 1):
        last_node_of_roatated = last_node_of_roatated.next
    head = last_node_of_roatated.next
    last_node_of_roatated.next = None
    return head

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = rotate(head, 3)
  print("Nodes of rotated LinkedList are: ", end='')
  result.print_list()


main()


