"""
 Insert Node at a specific position in a linked list
 head input could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""


# This is a "method-only" submission.
# You only need to complete this method.
def InsertNth(head, data, position):
    if position == 0:
        original_head = head
        head = Node(data)
        head.next = original_head
    else:
        current = head
        i = 1
        while (current.next != None and i < position):
            current = current.next
            i += 1
        new_node = Node(data, current.next)
        current.next = new_node
    return head
