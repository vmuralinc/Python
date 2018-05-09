class SllNode():
    value = None
    next = None

    def __init__(self, value, next=None):
        if value:
            self.value = value
            self.next = next
        else:
            raise ValueError('value to be added cannot be None')

    def __repr__(self):
        if self:
            return str(self.value)
        else:
            raise ValueError('Node is empty')


class SingleLinkedList():
    head = None

    def __init__(self, value=None):
        if value:
            self.head = SllNode(value)

    def __repr__(self):
        if self.head == None:
            raise ValueError('The list is empty')
        string = str(self.head)
        temp = self.head.next
        while temp != None:
            string += " -> " + str(temp)
            temp = temp.next
        return string

    def __str__(self):
        if self.head == None:
            raise ValueError('The list isempty')
        string = str(self.head)
        temp = self.head.next
        while temp != None:
            string += ", " + str(temp)
            temp = temp.next
        return string

    def addFirst(self, value):
        if value:
            if self.head == None:
                self.head = SllNode(value)
            else:
                self.head = SllNode(value, self.head)
        else:
            raise ValueError('value to be added cannot be None')

    def addLast(self, value):
        if value:
            if self.head == None:
                self.head = SllNode(value)
            else:
                temp = self.head
                while temp.next != None:
                    temp = temp.next
                temp.next = SllNode(value)
        else:
            raise ValueError('value to be added cannot be None')

    def removeFirst(self):
        if self.head != None:
            temp = self.head
            self.head = self.head.next
            return temp.value
        else:
            return None

    def removeLast(self):
        if self.head != None:
            temp = self.head
            if temp.next == None:
                self.head = None
                return temp.value 
            while temp.next.next != None:
                temp = temp.next
            value = temp.next.value
            temp.next = None
            return value
        else:
            return None
