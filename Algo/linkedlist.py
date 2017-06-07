a,b,c,d = None, None, None, None

class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None


    def __str__(self):
        if self.next == None:
            return self.value
        else:
            return self.value + str(self.next)

def delete_node(node):
    node.value = node.next.value
    node.next = node.next.next

def setup(a,b,c,d):
    a = LinkedListNode('A')
    b = LinkedListNode('B')
    c = LinkedListNode('C')
    d = LinkedListNode('D')

    a.next = b
    b.next = c
    c.next = d

    return a


delete_node(a)
assert(setup(a,b,c,d) == 'BCD')
