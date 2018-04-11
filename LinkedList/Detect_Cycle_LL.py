"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    if head is not None and head.next is not None:
        s = set()
        current = head
        while (current):
            if (current in s):
                return True
            s.add(current)
            current = current.next
        return False
