from accessify import private

from exception import StackEmpty, LimitException, StackMaxSize


class Stack:
    def __init__(self, size):
        self.size = size
        self.__stack = [None] * size
        self.tail = 0

    def get_stack(self):
        return list(self.__stack)

    def append(self, element):
        if self.tail > self.size: raise StackMaxSize(self.tail)
        self.__stack[self.tail] = element
        self.tail += 1

    def pop(self):
        if self.tail == 0: raise StackEmpty(self.tail)
        self.__stack[self.tail - 1] = None
        self.tail -= 1


class Deque:
    def __init__(self, limit):
        self.__deque = [None] * limit
        self.limit = limit
        self.head = 0
        self.tail = 0
        self.size = 0

    def get_stack(self):
        return list(self.__deque)

    @private
    def _limit_validator(self):
        if self.size == self.limit:
            raise LimitException(self.limit)

    @private
    def _empty_validator(self):
        if self.size == 0:
            raise StackEmpty(self.limit)

    @private
    def _empty_reset(self):
        if self.size == 0:
            self.head = 0
            self.tail = 0

    def append_right(self, element):
        self._limit_validator()
        if self.size == 0: self.head += 1
        self.tail = (self.tail + 1) % self.limit
        self.__deque[self.tail] = element
        self.size += 1

    def append_left(self, element):
        self._limit_validator()
        if self.size > 0: self.head = (self.head - 1) % self.limit
        self.__deque[self.head] = element
        self.size += 1

    def pop_right(self):
        self._empty_validator()
        self.__deque[self.tail] = None
        self.tail = (self.tail - 1) % self.limit
        self.size -= 1
        self._empty_reset()

    def pop_left(self):
        self._empty_validator()
        self.__deque[self.head] = None
        self.head = (self.head + 1) % self.limit
        self.size -= 1
        self._empty_reset()


class DoubleLinkedList:
    class Node:
        def __init__(self, head, next=None, prev=None):
            self.head = head
            self.next = next
            self.prev = prev

    def __init__(self, limit=None):
        self.head = None
        self.elements = None
        self.limit = limit
        self.size = 0

    def max_size(self):
        if self.limit is not None and (len(self.elements) > self.limit or self.size > self.limit):
            raise LimitException(self.limit)

    def display(self):
        while self.head.next:
            print(self.head.head)
            self.head = self.head.next
        print(self.head.head)

    @staticmethod
    def get_node_by_index(node, index):
        while index:
            node = node.next
            index -= 1
        return node

    def add(self, element):
        self.size += 1
        self.max_size()
        new_node = self.Node(element)
        new_node.next = self.head
        new_node.next.prev = new_node
        self.head = new_node

    def add_by_index(self, element, index):
        new_node = self.Node(element)
        head = self.get_node_by_index(self.head, index)
        if index == 0:
            new_node.next = head
            self.head = new_node
        else:
            if head.next is None:
                head.next = new_node
                new_node.prev = head
            else:
                head.prev.next = new_node
                new_node.next = head
                new_node.prev = head.prev

    def delete(self):
        next = self.head.next
        self.head = next
        self.size -=1

    def delete_by_index(self, index):
        node = self.get_node_by_index(self.head, index)
        self.size -= 1
        if index == 0:
            self.head = node.next
        else:
            prev = node.prev
            next = node.next
            node.prev.next = next
            if node.next is not None:
                node.next.prev = prev

    def rever(self):
        current = self.head
        while current:
            save = current.next
            if current.next is None:
                current.next = current.prev
                current.prev = save
                self.head = current
                return self.head
            current.next = current.prev
            current.prev = save
            current = current.prev

    def list_to_linked_list(self, elements):
        self.elements = elements
        self.max_size()
        self.size = len(self.elements)
        if isinstance(self.elements, list):
            for element in self.elements:
                new_node = self.Node(element)
                new_node.next = self.head
                self.head = new_node
                if self.head.next is not None: self.head.next.prev = self.head

