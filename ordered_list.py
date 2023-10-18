from dataclasses import dataclass

@dataclass
class Node:
    value: int
    prev_node: None
    next_node: None


@dataclass
class DoublyOrderedList:
    """
    A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of
    list
    """
    head: 'Node' = None
    tail: 'Node' = None

    def is_empty(self):
        # Returns True if OrderedList is empty O(1)
        if self.head is None:
            return True

    def add(self, value):
        # Adds an item to OrderedList, in the proper location based on ordering of items
        # from lowest (at head of list) to highest (at tail of list) and returns True.
        # If the item is already in the list, do not add it again and return False.
        # MUST have O(n) average-case performance
        new_node = Node(value, None, None)
        current_node = self.head
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif self.head.next_node is None:
            self.head.next_node = new_node
            self.tail = new_node
            new_node.prev_node = self.head
        else:
            while current_node.next_node is not None:
                if current_node.next_node.value > new_node.value or current_node.next_node is None:
                    new_node.prev_node = current_node
                    new_node.next_node = current_node.next_node
                    if current_node.next_node is not None:
                        current_node.next_node.prev_node = new_node
                    current_node.next_node = new_node
                    if new_node.next_node is None:
                        self.tail = new_node
                else:
                    current_node = current_node.next_node

    def remove(self, value):
        # Removes the first occurrence of an item from OrderedList. If item is removed (was
        # in the list)
        # returns True. If item was not removed (was not in the list) returns False
        # MUST have O(n) average-case performance'''
        if self.head is None:  # If list is empty
            return True
        if self.head == self.tail and self.head.value == value:  # If list has one node
            self.head = None
            self.tail = None
            return True

        # If list has more than one node
        current_node = self.head  # Start at the head
        while current_node is not None:
            if current_node.value == value:
                if current_node == self.head:  # If head holds value, remove head
                    self.head = current_node.next_node
                    self.head.prev_node = None
                    return True
                elif current_node == self.tail:  # If tail holds value, remove tail
                    self.tail = current_node.prev_node
                    self.tail.next_node = None
                    return True
                else:  # First connect prev_node to next_node, then next_node to prev_node to skip over current_node
                    current_node.prev_node.next_node = current_node.next_node
                    current_node.next_node.prev_node = current_node.prev_node
                    return True
            current_node = current_node.next_node  # Traverse forward

        return False

    def index(self, item):
        """Returns index of the first occurrence of an item in OrderedList (assuming head of
        list is index 0).
        If item is not in list, return None
        MUST have O(n) average-case performance"""
        current_node = self.head
        current_index = 0
        while current_node is not None:
            if current_node.value == item:
                return current_index
            else:
                current_index += 1
                current_node = current_node.next_node
        return None

    def pop(self, index):
        # Removes and returns item at index (assuming head of list is index 0).
        # If index is negative or >= size of list, raises IndexError
        # MUST have O(n) average-case performance
        current_node = self.head
        current_index = 0
        if index == 0:
            if current_node.next_node is not None:
                self.head = current_node.next_node
            self.head.prev_node = None
            temp = self.head.value
            del self.head
            del self.tail
            return temp
            # return current_node.value
        while current_node is not None:
            if current_index == index:
                if current_node.next_node is not None:
                    current_node.prev_node.next_node = current_node.next_node
                    current_node.next_node.prev_node = current_node.prev_node
                else:
                    self.tail = current_node.prev_node
                    self.tail.nextNode = None
                return current_node.value
            else:
                current_index += 1
                current_node = current_node.next_node

    def search(self, item):
        # Searches OrderedList for item, returns True if item is in list, False otherwise
        # To practice recursion, this method must call a RECURSIVE method that
        # will search the list
        # MUST have O(n) average-case performance'''
        current_node = self.head
        return self._search_recursive(item, current_node)

    def _search_recursive(self, item, cur):
        if cur is None:
            return False
        elif cur.value == item:  # Base case for finding value
            return True
        elif cur == self.tail:  # If we traversed to the end of the list and didn't find value
            return False

        return self._search_recursive(item, cur.next_node)  # Recurse through with the next node

    def python_list(self):
        # Return a Python list representation of OrderedList, from head to tail
        # For example, list with integers 1, 2, and 3 would return [1, 2, 3]
        # MUST have O(n) performance'''
        result = []
        cur_node = self.head
        while cur_node is not None:
            result.append(cur_node.value)
            cur_node = cur_node.next_node
        return result


    # TODO
    def python_list_reversed(self):
        # Return a Python list representation of OrderedList, from tail to head, using
        # recursion
        # For example, list with integers 1, 2, and 3 would return [3, 2, 1]
        # To practice recursion, this method must call a RECURSIVE method that
        # will return a reversed list
        # MUST have O(n) performance'''
        pass

    def size(self):
        cur_node = self.head  # Start at head
        size = self._size_recursive(0, cur_node)  # Start with counter = 0

        return size  # Return size

    def _size_recursive(self, count, cur_node):
        if cur_node is None:  # Base Case
            return count  # Return final count without adjustment

        return self._size_recursive(count + 1, cur_node.next_node)  # Traverse forward one and increase node count
