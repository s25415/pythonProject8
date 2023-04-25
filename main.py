import student

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        ret = ''
        current = self.head
        while current is not None:
            ret += str(current)
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
                if current.nextE == e:
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
                    if func(e, current.nextE):
                        e.nextE = current.nextE
                        current.nextE = e
                        self.size += 1
                        return True
                current = current.nextE
            return False


if __name__ == '__main__':
    lista = MyLinkedList()
    student1 = student.Student("lukasz@gmail.com", "lukasz", "kwasniewicz")
    student2 = student.Student("lukasz@gmail.com", "adam", "zdun")
    lista.append(student1, lambda x, y, func: student.Student.compareStudentsNames(x, y))
    lista.append(student2, lambda x, y, func: student.Student.compareStudentsNames(x, y))

    lista.delete(student)
    print(lista)
