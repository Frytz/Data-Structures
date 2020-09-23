class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self,value):
        new_node = Node(value)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            selfhead = new_node

    def add_to_tail(self, value):
        new_node = Node(value)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove_tail(self):
        if not self.head and not self.tail:
            return None
        elif self.head == self.tail:
            value = self.tail.value
            self.head = None
            self.tail = None
            return value
        else:
            value = self.tail.value
            current_node = self.head
            while current_node.next != self.tail:
                current_node = current_node.next
            self.tail = current_node
            self.tail.next = None
            return value

    def remove_head(self):
        if not self.head and not self.tail:
            return None
        elif self.head == self.tail:
            value = self.head.value
            self.head = None
            self.tail = None
            return value
        else:
            value = self.head.value
            self.head = self.head.next
            return value
