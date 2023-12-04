from typing import List, Any

class Node:
    def __init__(self, value: Any = None):
        """
        Initialize a node with a given value.

        Parameters:
        - value (Any): The value to be stored in the node.
        """
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, values: List[Any]):
        """
        Initialize a linked list with a list of values.

        Parameters:
        - values (List[Any]): The list of values to create the linked list.
        """
        self.root = None
        self.create_linked_list(values)

    def create_linked_list(self, values: List[Any]):
        """
        Create a linked list from a list of values.

        Parameters:
        - values (List[Any]): The list of values to create the linked list.
        """
        if not values:
            return

        self.root = Node(values[0])
        curr = self.root

        for value in values[1:]:
            curr.next = Node(value)
            curr = curr.next

    def print_linked_list(self):
        """
        Print the elements of the linked list.
        """
        curr = self.root
        while curr:
            print(curr.value, end=" ")
            curr = curr.next
        print("\n")

    def reverse_linked_list(self):
        """
        Reverse the linked list in-place.

        Explanation:
        - The method uses a classic iterative approach to reverse a linked list.
        - It maintains three pointers: prev, curr, and next_node.
        - In each iteration, it reverses the direction of the current node's next pointer,
          then moves the prev, curr, and next_node pointers one step forward.
        - Finally, the root of the linked list is updated to the last node, making it the new head.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        prev = None
        curr = self.root

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.root = prev

if __name__ == "__main__":
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    linked_list = LinkedList(values)

    print("Original Linked List:")
    linked_list.print_linked_list() # 1 2 3 4 5 6 7 8 9 

    linked_list.reverse_linked_list()

    print("\nReversed Linked List:")
    linked_list.print_linked_list() # 9 8 7 6 5 4 3 2 1
