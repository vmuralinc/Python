"""Contains the single linked list and single linked list node classes"""


class SllNode():
    """Basic unit of a Single linked list"""
    value = None
    next = None

    def __init__(self, value, next=None):
        """Initialize the node

        Keyword arguments:
        value -- the value of the node (default is None, will raise ValueError)
        next -- the pointer to the next node (default is None)
        """
        if value:
            self.value = value
            self.next = next
        else:
            # Raises ValueError if the value is not passed in arguments
            raise ValueError('value to be added cannot be None')

    def __repr__(self):
        """Returns the value in string format"""
        if self.value:
            return str(self.value)
        else:
            # Raises ValueError if the node value is empty
            raise ValueError('Node value is empty')


class SingleLinkedList():
    """Implements a single linked list"""
    head = None

    def __init__(self, value=None):
        """Initializes a head node with value and next node as None

        Keyword arguments:
        value -- value of the head node (default is None)
        """
        if value:
            self.head = SllNode(value)

    def __repr__(self):
        """Returns a string of the list values separated by '->'"""
        if self.head is None:
            raise ValueError('The list is empty')
        string = str(self.head)
        temp = self.head.next
        while temp is not None:
            string += " -> " + str(temp)
            temp = temp.next
        return string

    def __str__(self):
        """Returns a string of the list values separated by ','"""
        if self.head is None:
            raise ValueError('The list isempty')
        string = str(self.head)
        temp = self.head.next
        while temp is not None:
            string += ", " + str(temp)
            temp = temp.next
        return string

    def addFirst(self, value):
        """Adds a new node to the head of the linked list"""
        if value:
            if self.head is None:
                self.head = SllNode(value)
            else:
                self.head = SllNode(value, self.head)
        else:
            raise ValueError('value to be added cannot be None')

    def addLast(self, value):
        """Adds a new node to the end of the linked list"""
        if value:
            if self.head is None:
                self.head = SllNode(value)
            else:
                temp = self.head
                while temp.next is not None:
                    temp = temp.next
                temp.next = SllNode(value)
        else:
            raise ValueError('value to be added cannot be None')

    def removeFirst(self):
        """Removes a node from the head of the list"""
        if self.head is not None:
            temp = self.head
            self.head = self.head.next
            return temp.value
        else:
            return None

    def removeLast(self):
        """Removes a node from the end of the list"""
        if self.head is not None:
            temp = self.head
            if temp.next is None:
                self.head = None
                return temp.value
            while temp.next.next is not None:
                temp = temp.next
            value = temp.next.value
            temp.next = None
            return value
        else:
            return None
