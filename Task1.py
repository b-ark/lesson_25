# Implement append, index, pop, insert methods for UnorderedList.
# Also implement a slice method, which will take two parameters `start` and `stop`,
# and return a copy of the list starting at the position and going up to but not including the stop position.
from node import Node


class UnorderedList:

    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self._head)
        self._head = temp

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def search(self, item):
        current = self._head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        current = self._head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self._head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def __repr__(self):
        representation = "<UnorderedList: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"

    def __str__(self):
        return self.__repr__()

    def append(self, item):
        temp = Node(item)
        temp.set_next(self._head)
        self._head = temp

    def index(self, item):
        index = -1
        current = self._head
        found = False
        while current is not None and not found:
            index += 1
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        if found is False:
            return 'item not found'
        return index

    def insert(self, index, item):
        if index < 0:
            index = self.size() + index + 1
        if index > self.size():
            raise IndexError('IndexError: sequence subscript is out of range')
        current = self._head
        previous = None
        count = 0
        found = False
        while not found:
            if count == index:
                found = True
            else:
                count += 1
                previous = current
                current = current.get_next()
        if previous is None:
            self.add(item)
        else:
            temp = Node(item)
            temp.set_next(current)
            previous.set_next(temp)

    def slice(self, start, stop):
        if start < 0 or stop > self.size():
            raise IndexError('IndexError: sequence subscript is out of range')
        if start > stop:
            raise ValueError('ValueError: starting position is larger then stopping')
        new_list = UnorderedList()
        current = self._head
        count = 0
        while True:
            if count == start:
                count = 0
                while count < stop - start:
                    new_list.insert(count, current.get_data())
                    current = current.get_next()
                    count += 1
                return new_list
            else:
                current = current.get_next()
                count += 1


def main():
    my_list = UnorderedList()

    my_list.add(31)
    my_list.add(77)
    my_list.add(17)
    my_list.add(93)
    my_list.add(26)
    my_list.add(54)

    print(my_list.size())
    print(my_list)
    print(my_list.search(93))
    print(my_list.search(100))

    my_list.add(100)
    print(my_list.search(100))
    print(my_list.size())

    my_list.remove(54)
    print(my_list.size())
    my_list.remove(93)
    print(my_list.size())
    my_list.remove(31)
    print(my_list.size())
    print(my_list.search(93))
    my_list.append(18)
    print(my_list)
    print(my_list.index(100))
    my_list.insert(-1, 99)
    print(my_list)
    new_list = my_list.slice(0, 3)
    print(new_list)


if __name__ == "__main__":
    try:
        main()
    except IndexError as massage:
        print(massage)
