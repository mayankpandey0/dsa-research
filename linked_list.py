"""Implementation of a Singly Linked List Data Structure."""


class Node:
    # pylint: disable=too-few-public-methods
    """A node in a singly linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    """Basic implementation of a singly linked list."""

    def __init__(self):
        self.head = None

    def append(self, data):
        """Add a new node to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def search(self, target):
        """Search for a value in the list. Returns True if found, False otherwise."""
        current = self.head
        while current:
            if current.data == target:
                return True
            current = current.next
        return False

    def to_list(self):
        """
        Helper method to convert the linked list to a standard Python list
        (useful for testing).
        """
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
