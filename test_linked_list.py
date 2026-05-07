from linked_list import SinglyLinkedList

def test_empty_list():
    ll = SinglyLinkedList()
    assert ll.to_list() == []
    assert ll.search(10) is False

def test_append_single_item():
    ll = SinglyLinkedList()
    ll.append(5)
    assert ll.to_list() == [5]
    assert ll.search(5) is True

def test_append_multiple_items():
    ll = SinglyLinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert ll.to_list() == [1, 2, 3]

def test_search_item():
    ll = SinglyLinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    
    assert ll.search(20) is True
    assert ll.search(100) is False
