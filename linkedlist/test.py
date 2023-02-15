import unittest
from linkedlist.main import LinkedList

class TestCase(unittest.TestCase):

    def test_add_item(self):
        list = LinkedList()
        list.add(1)
        self.assertEquals(list.first().value, 1)

    def test_add_2_items(self):
        list = LinkedList()
        list.add(1)
        list.add(2)
        self.assertEquals(list.first().value, 1)
        self.assertEquals(list.first().next().value, 2)

    def test_add_3_items(self):
        list = LinkedList()
        list.add(1)
        list.add(2)
        list.add(3)
        self.assertEquals(list.first().value, 1)
        self.assertEquals(list.first().next().value, 2)
        self.assertEquals(list.first().next().next().value, 3)

    def test_access_by_index(self):
        list = LinkedList()
        list.add(1)
        list.add(2)
        list.add(3)
        list.add(4)
        self.assertEquals(list.index(3).value, 4)

    def test_list_len(self):
        list = LinkedList()
        list.add(1)
        list.add(2)
        list.add(3)
        list.add(4)
        self.assertEquals(list.len(), 4)

    def test_list_remove(self):
        list = LinkedList()
        list.add(1)
        list.add(2)
        list.add(3)
        list.add(4)
        self.assertEquals(list.len(), 4)
        self.assertEquals(list.last()._index, 3)
        list.remove(2)
        self.assertEquals(list.len(), 3)
        self.assertEquals(list.last()._index, 2)

    def test_list_remove_last(self):
        list = LinkedList()
        list.add(1)
        list.add(2)
        list.add(3)
        list.add(4)
        self.assertEquals(list.len(), 4)
        self.assertEquals(list.last()._index, 3)
        list.remove(3)
        self.assertEquals(list.len(), 3)
        self.assertEquals(list.last()._index, 2)

    def test_list_remove_last(self):
        list = LinkedList()
        list.add(1)
        list.add(2)
        list.add(3)
        list.add(4)
        self.assertEquals(list.len(), 4)
        self.assertEquals(list.last()._index, 3)
        list.remove(0)
        self.assertEquals(list.len(), 3)
        self.assertEquals(list.first().value, 2)

    def test_add_in_the_middle(self):
        list = LinkedList()
        list.add(1)
        list.add(2)
        list.add(3)
        self.assertEquals(list.index(1).value, 2)
        list.add(4, 1)
        self.assertEquals(list.index(1).value, 4)

    def test_add_in_the_start(self):
        list = LinkedList()
        list.add(1)
        list.add(2)
        list.add(3)
        self.assertEquals(list.index(0).value, 1)
        list.add(4, 0)
        self.assertEquals(list.index(0).value, 4)
