class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.root = None
    
    
    def insert(self,value):
        if self.root is None:
            self.root = Node(value)
        else:
            curr = self.root
            # To avoid tracking the last node, we need to keep track of
            last_node = curr
            while curr:
                last_node = curr
                curr = curr.next
            last_node.next = Node(value)
    
    def reverse(self):
        if self.root is None:
            return
        left = None
        curr = self.root
        while curr:
            # Track the next node
            right = curr.next
            # Change the current node's next chain with  it's left node
            curr.next = left
            # Update the left node
            left = curr 
            # Now go to the right node
            curr = right
        # Change the pointer to the last node
        self.root = left
    
    def print(self):
        if self.root is None:
            return
        curr = self.root
        while curr:
            print(curr.data)
            curr = curr.next


if __name__ == '__main__':
    values = [1, 2, 3, 4, 5, 6, 7]
    
    linkedlist = LinkedList()
    
    for value in values:
        linkedlist.insert(value)
    
    print("in order: ")
    linkedlist.print()
    print("-"*40)
    
    print("in reverse")
    linkedlist.reverse()
    linkedlist.print()
    print("-"*40)