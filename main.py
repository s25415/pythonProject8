class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        ret = ''
        current = self.head
        while current is not None:
            ret += str(current.data)
            current = current.nextE
        return ret

    def get(self, e):
        counter = 0
        current = self.head
        while current:
            if counter == e:
                return current
            counter += 1
            current = current.nextE
        return None

    def delete(self, e):
        current = self.head
        while current:
            if current.nextE is None:
                return False
            else:
                if current.nextE.data == e.data:
                    next = current.nextE.nextE
                    current.nextE = next
                    self.size -= 1
            current = current.nextE
        return None

    def append(self, e, func=None):

        if self.head is None:
            self.head = e
            return True
        else:
            if func is None:
                func = lambda x, y: x <= y
            current = self.head
            while current is not None:
                if current.nextE is None:
                    e.nextE = current.nextE
                    current.nextE = e
                    self.size += 1
                    return True
                else:
                    if func(e.data, current.nextE.data):
                        e.nextE = current.nextE
                        current.nextE = e
                        self.size += 1
                        return True
                current = current.nextE
            return False


class Element:
    def __init__(self, data=None, nextE=None):
        self.data = data
        self.nextE = nextE


if __name__ == '__main__':
    lista = MyLinkedList()
    lista.append(Element(1))
    lista.append(Element(4))
    lista.append(Element(8))
    lista.append(Element(3))
    lista.append(Element(2))

    lista.delete(Element(4))
    print(lista)
    print(lista.get(2).data)
