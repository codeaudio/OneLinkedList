class Node:
    def __init__(self, value=None):
        self.value = value
        self.nextvalue = None


class LinkedList:
    def __init__(self):
        self.head = None

    def sort_add(self, newvalue):
        newnode = Node(newvalue)
        if self.head is None:
            self.head = newnode
        elif self.head.value < newvalue:
            old_head = self.head
            self.head = newnode
            self.head.nextvalue = old_head
        else:
            node = self.head
            while node:
                if (
                        (node.value > newvalue and node.nextvalue is None) or
                        (node.value > newvalue > node.nextvalue.value)
                ):
                    nodenext = node.nextvalue
                    node.nextvalue = newnode
                    newnode.nextvalue = nodenext
                node = node.nextvalue

    def add_to_end(self, newvalue):
        newnode = Node(newvalue)
        if self.head is None:
            self.head = newnode
        else:
            head_node = self.head
            while head_node.nextvalue:
                head_node = head_node.nextvalue
            head_node.nextvalue = newnode

    def delete(self, index):
        node = self.head
        i = 0
        if index == 0:
            self.head = node.nextvalue
        else:
            while node.nextvalue and i != index:
                if i == index - 1:
                    nodenext = node.nextvalue
                    nodenextnext = nodenext.nextvalue
                    node.nextvalue = nodenextnext
                else:
                    node = node.nextvalue
                i += 1

    def get_index(self, el):
        node = self.head
        i = 0
        if node.value == el: return 0
        while node.nextvalue:
            node = node.nextvalue
            i += 1
            if el == node.value:
                return i

    def search_for_insert(self, index, node, newnode):
        if node.nextvalue is None:
            node.nextvalue = newnode
        if index == 1:
            nodenext = node.nextvalue
            node.nextvalue = newnode
            newnode.nextvalue = nodenext
        else:
            return self.search_for_insert(index - 1, node.nextvalue, newnode)

    def insert(self, index, el):
        newnode = Node(el)
        if index == 0:
            old_head = self.head
            self.head = newnode
            newnode.nextvalue = old_head
            return
        self.search_for_insert(index, self.head, newnode)

    def display(self):
        node = self.head
        while node.nextvalue:
            print(node.value)
            node = node.nextvalue
        print(node.value)

    def get_list_linked_list_value(self):
        node = self.head
        arr = []
        while node.nextvalue:
            arr.append(node.value)
            node = node.nextvalue
        arr.append(node.value)
        return arr[::-1]

    def clear_all_child_node(self):
        self.head.nextvalue = None

    def clear(self):
        self.head = None


node = LinkedList()

node.sort_add(4)
node.sort_add(2)
node.sort_add(223)
node.sort_add(-223)
node.sort_add(9)
node.insert(4, 999)
node.delete(0)
node.add_to_end(1212)
node.add_to_end(1212)
node.add_to_end(1212)
node.clear_all_child_node()
node.add_to_end(4)
node.insert(0, 1)
node.clear_all_child_node()
node.display()
print(node.get_list_linked_list_value())
