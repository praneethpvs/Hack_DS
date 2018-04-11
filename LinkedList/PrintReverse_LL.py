"""
 Print elements of a linked list in reverse order as standard output
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node


"""


def ReversePrint(head):
    reverse_list = []
    if head is not None:
        if head.next is None:
            print head.data
        else:
            current = head
            while (current is not None):
                reverse_list.insert(0, current.data)
                current = current.next
            for val in reverse_list:
                print val
