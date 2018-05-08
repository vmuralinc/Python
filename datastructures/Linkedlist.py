class Node():
    value = None
    next = None

    def __init__(self, value, next=None):
        if value:
            self.value = value
            self.next = next
        else:
            raise ValueError('value to be added cannot be None')

    def __repr__(self):
        return str(self.value)


class Linkedlist():
    head = None

    def __init__(self, value):
        self.head = Node(value)

    def __repr__(self):
        string = str(self.head)
        temp = self.head.next
        while temp != None:
            string += " -> " + str(temp)
            temp = temp.next
        return string

    def __str__(self):
        string = str(self.head)
        temp = self.head.next
        while temp != None:
            string += ", " + str(temp)
            temp = temp.next
        return string

    def add(self, value):
        if value:
            if self.head == None:
                self.head = Node(value)
            else:
                temp = self.head
                while temp.next != None:
                    temp = temp.next
                temp.next = Node(value)
        else:
            raise ValueError('value to be added cannot be None')
