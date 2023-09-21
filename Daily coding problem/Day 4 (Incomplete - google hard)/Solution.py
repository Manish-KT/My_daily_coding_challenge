class Node:
    def __init__(self, element):
        self.element = element
        self.both = None


class XORLinkedList:
    def __init__(self):
        self.head = None

    def add(self, element):
        new_node = Node(element)
        if self.head is None:
            self.head = new_node
            new_node.both = None
        else:
            current = self.head
            prev = None
            while current.both is not None:
                next_node_address = id(prev) ^ id(current.both)
                prev = current
                current = dereference_pointer(next_node_address)
            current.both = id(prev) ^ id(new_node)
            new_node.both = id(current) ^ None

    def get(self, index):
        current = self.head
        prev = None
        i = 0

        while current is not None and i < index:
            next_node_address = id(prev) ^ id(current.both)
            prev = current
            current = dereference_pointer(next_node_address)
            i += 1

        if current is not None:
            return current.element
        else:
            raise IndexError("Index out of bounds")


# Example usage:
xor_list = XORLinkedList()
xor_list.add(10)
xor_list.add(20)
xor_list.add(30)

# Get the element at index 1 (which should be 20)
element_at_index_1 = xor_list.get(1)
print(element_at_index_1)  # Output: 20
