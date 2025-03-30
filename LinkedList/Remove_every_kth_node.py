
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def remove_every_kth_node(self, k):
        if k <= 0:
            raise ValueError("k must be a positive integer")
        if self.head is None:
            return
        
        current = self.head
        prev = None
        count = 1


        while current is not None:
            if count % k == 0:
                if prev is not None:
                    prev.next = current.next
                current = current.next
                count += 1
                continue

            prev = current
            current = current.next
            count += 1


    def traverse(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next


sll = SinglyLinkedList()
n1 = Node(6)
sll.head = n1
n2 = Node(7)
n1.next = n2
n3 = Node(8)
n2.next = n3
n4 = Node(9)
n3.next = n4
n5 = Node(10)
n4.next = n5
n6 = Node(11)
n5.next = n6
n7 = Node(12)
n6.next = n7

sll.remove_every_kth_node(3)
sll.traverse()
