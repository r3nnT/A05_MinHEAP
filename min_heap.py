# Name: Tyler Renn
# OSU Email: rennt@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: A05
# Due Date: 05/29/2023
# Description: Implement the MinHeap class using a dynamic array as the underlying
# Data structure


from dynamic_array import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initialize a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        heap_data = [self._heap[i] for i in range(self._heap.length())]
        return 'HEAP ' + str(heap_data)

    def add(self, node: object) -> None:
        """
        This method adds a new object to the MinHeap while maintaining heap property.
        """
        self._heap.append(node)
        current = self._heap.length() - 1
        parent = (current - 1) // 2

        while current > 0 and self._heap[current] < self._heap[parent]:
            self._heap[current], self._heap[parent] = self._heap[parent], \
            self._heap[current]
            current = parent
            parent = (current - 1) // 2

    def is_empty(self) -> bool:
        """
        This method returns True if the heap is empty; otherwise, it returns False.

        """

        if self._heap.length() == 0:
            return True

        return False

    def get_min(self) -> object:
        """
        This method returns an object with the minimum key,
        without removing it from the heap.
        If the heap is empty, the method raises a MinHeapException.
        """
        if self.is_empty():
            raise MinHeapException("MinHeap is empty")

        return self._heap.get_at_index(0)

    def remove_min(self) -> object:
        """
        This method returns an object with the minimum key,
        and removes it from the heap.
        If the heap is empty, the method raises a MinHeapException.
        """
        if self.is_empty():
            raise MinHeapException("MinHeap is empty")

        min_key = self._heap[0]
        last_element = self._heap[self._heap.length() - 1]
        self._heap[0] = last_element
        self._heap.remove_at_index(self._heap.length() - 1)

        current = 0
        while True:
            left_child = 2 * current + 1
            right_child = 2 * current + 2
            smallest_child = current

            if left_child < self._heap.length() and self._heap[left_child] < \
                    self._heap[smallest_child]:
                smallest_child = left_child
            if right_child < self._heap.length() and self._heap[right_child] < \
                    self._heap[smallest_child]:
                smallest_child = right_child

            if smallest_child != current:
                self._heap[current], self._heap[smallest_child] = self._heap[
                    smallest_child], self._heap[current]
                current = smallest_child
            else:
                break

        return min_key

    def build_heap(self, da: DynamicArray) -> None:
        """
        his method receives a DynamicArray with objects in any order,
        and builds a proper
        MinHeap from them. The current content of the MinHeap is overwritten.
        """

        self.clear()


        # Copy the elements from the DynamicArray to the MinHeap's underlying DynamicArray
        self._heap = DynamicArray(da)

        # Get the length of the DynamicArray
        n = self._heap.length()

        # Iterate over each parent node starting from the last parent
        for i in range(n // 2 - 1, -1, -1):
            percolate_down(self._heap, i)


    def size(self) -> int:
        """
        This method returns the number of items currently stored in the heap.
        """
        return self._heap.length()

    def clear(self) -> None:
        """
        This method clears the contents of the heap.
        """
        self._heap = DynamicArray()


def heapsort(da: DynamicArray) -> None:
    """
    TODO: Write this implementation
    """
    pass


# It's highly recommended that you implement the following optional          #
# function for percolating elements down the MinHeap. You can call           #
# this from inside the MinHeap class. You may edit the function definition.  #

def percolate_down(da: DynamicArray, parent: int) -> None:
    """
    TODO: Write your implementation
    """
    n = da.length()
    smallest = parent

    while True:
        left = 2 * parent + 1
        right = 2 * parent + 2

        # Compare the parent with its left child
        if left < n and da[left] < da[smallest]:
            smallest = left

        # Compare the parent with its right child
        if right < n and da[right] < da[smallest]:
            smallest = right

        # If the smallest value is not the parent, swap them and update the parent index
        if smallest != parent:
            da[parent], da[smallest] = da[smallest], da[parent]
            parent = smallest
        else:
            break


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - is_empty example 1")
    print("-------------------")
    h = MinHeap([2, 4, 12, 56, 8, 34, 67])
    print(h.is_empty())

    print("\nPDF - is_empty example 2")
    print("-------------------")
    h = MinHeap()
    print(h.is_empty())

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty() and h.is_empty() is not None:
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)

    print("--------------------------")
    print("Inserting 500 into input DA:")
    da[0] = 500
    print(da)

    print("Your MinHeap:")
    print(h)
    if h.get_min() == 500:
        print("Error: input array and heap's underlying DA reference same object in memory")

    print("\nPDF - heapsort example 1")
    print("------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - heapsort example 2")
    print("------------------------")
    da = DynamicArray(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - size example 1")
    print("--------------------")
    h = MinHeap([100, 20, 6, 200, 90, 150, 300])
    print(h.size())

    print("\nPDF - size example 2")
    print("--------------------")
    h = MinHeap([])
    print(h.size())

    print("\nPDF - clear example 1")
    print("---------------------")
    h = MinHeap(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(h)
    print(h.clear())
    print(h)
