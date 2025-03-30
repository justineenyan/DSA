
#Program to illustrate how to find the middle element
#of a linked list using Floyd's cycle Finding Algorithm


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        
    
    def getMiddleNode(self):
        slow_ptr = self.head
        fast_ptr = self.head

        while fast_ptr is not None and fast_ptr.next is not None:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next

        return slow_ptr.data
    
sll = SinglyLinkedList()
n1 = Node(1)
sll.head = n1
n2 = Node(2)
n1.next = n2
n3 = Node(3)
n2.next = n3
n4 = Node(4)
n3.next = n4
n5 = Node(5)
n4.next = n5
n6 = Node(6)
n5.next = n6

print(sll.getMiddleNode()) #Output: 3
