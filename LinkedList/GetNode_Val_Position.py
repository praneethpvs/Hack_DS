# Body
"""
 Get Node data of the Nth Node from the end.
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the node data of the linked list in the below method.
"""


def GetNode(head, position):
    temp_list = []
    if head is not None:
        current = head
        while (current):
            temp_list.append(current.data)
            current = current.next
    return temp_list[len(temp_list) - position - 1]
