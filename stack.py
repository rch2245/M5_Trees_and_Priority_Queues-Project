"""Stack ADT used by the binary expression tree."""


class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        """Push an item onto the top of the stack."""
        self._data.append(item)

    def pop(self):
        """Remove and return the top item."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def top(self):
        """Return the top item without removing it."""
        if self.is_empty():
            raise IndexError("top from empty stack")
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)
