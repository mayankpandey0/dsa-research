"""Unit tests for the Singly Linked List implementation."""

from linked_list import SinglyLinkedList


def test_empty_list():
    """Test behavior of an empty linked list."""
    ll = SinglyLinkedList()
    assert not ll.to_list()
    assert ll.search(10) is False


def test_append_single_item():
    """Test appending a single item to the linked list."""
    ll = SinglyLinkedList()
    ll.append(5)
    assert ll.to_list() == [5]
    assert ll.search(5) is True


def test_append_multiple_items():
    """Test appending multiple items to the linked list."""
    ll = SinglyLinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert ll.to_list() == [1, 2, 3]


def test_search_item():
    """Test searching for existing and non-existing items in the linked list."""
    ll = SinglyLinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)

    assert ll.search(20) is True
    assert ll.search(100) is False
