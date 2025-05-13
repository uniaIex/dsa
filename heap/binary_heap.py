class MinHeap:
    def __init__(self):
        # Initialize an empty list to store the heap
        self.heap = []
    
    def parent(self, i):
        """Return the parent index of the node at index i"""
        return (i - 1) // 2
    
    def left_child(self, i):
        """Return the left child index of the node at index i"""
        return 2 * i + 1
    
    def right_child(self, i):
        """Return the right child index of the node at index i"""
        return 2 * i + 2
    
    def has_parent(self, i):
        """Check if node at index i has a parent"""
        return self.parent(i) >= 0
    
    def has_left_child(self, i):
        """Check if node at index i has a left child"""
        return self.left_child(i) < len(self.heap)
    
    def has_right_child(self, i):
        """Check if node at index i has a right child"""
        return self.right_child(i) < len(self.heap)
    
    def swap(self, i, j):
        """Swap elements at indices i and j"""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def insert(self, value):
        """Insert a new value into the heap"""
        # Add the element to the end of the heap
        self.heap.append(value)
        # Fix the heap property by bubbling up
        self._heapify_up(len(self.heap) - 1)
    
    def extract_min(self):
        """Remove and return the minimum element from the heap"""
        if not self.heap:
            return None
        
        # Store the minimum value to return later
        min_value = self.heap[0]
        
        # Move the last element to the root
        last_element = self.heap.pop()
        
        if self.heap:
            self.heap[0] = last_element
            # Fix the heap property by bubbling down
            self._heapify_down(0)
        
        return min_value
    
    def peek(self):
        """Return the minimum element without removing it"""
        if not self.heap:
            return None
        return self.heap[0]
    
    def _heapify_up(self, index):
        """Move element up the heap to maintain the heap property"""
        # While the element has a parent and is smaller than its parent
        while (self.has_parent(index) and 
               self.heap[index] < self.heap[self.parent(index)]):
            # Swap with parent
            parent_index = self.parent(index)
            self.swap(index, parent_index)
            # Move up to the parent index
            index = parent_index
    
    def _heapify_down(self, index):
        """Move element down the heap to maintain the heap property"""
        # While the element has at least one child
        while self.has_left_child(index):
            # Find the smaller child
            smaller_child_index = self.left_child(index)
            if (self.has_right_child(index) and 
                self.heap[self.right_child(index)] < self.heap[smaller_child_index]):
                smaller_child_index = self.right_child(index)
            
            # If element is smaller than its smallest child, heap property is satisfied
            if self.heap[index] <= self.heap[smaller_child_index]:
                break
            
            # Otherwise, swap with smaller child
            self.swap(index, smaller_child_index)
            # Move down to the child index
            index = smaller_child_index
    
    def build_heap(self, array):
        """Build a heap from an array of elements"""
        self.heap = array.copy()
        # Start from the last non-leaf node and heapify down
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._heapify_down(i)
    
    def size(self):
        """Return the size of the heap"""
        return len(self.heap)
    
    def is_empty(self):
        """Check if heap is empty"""
        return len(self.heap) == 0

# Example usage
if __name__ == "__main__":
    # Create a new min heap
    heap = MinHeap()
    
    # Insert elements
    elements = [4, 8, 2, 9, 5, 1, 6]
    print(f"Inserting elements: {elements}")
    for element in elements:
        heap.insert(element)
        print(f"After inserting {element}: {heap.heap}")
    
    # Extract minimum elements one by one
    print("\nExtracting elements:")
    while not heap.is_empty():
        min_val = heap.extract_min()
        print(f"Extracted min: {min_val}, Remaining heap: {heap.heap}")
    
    # Build heap from an array
    print("\nBuilding heap from array:")
    array = [10, 3, 6, 14, 8, 1, 7]
    print(f"Original array: {array}")
    heap.build_heap(array)
    print(f"Heap after building: {heap.heap}")
    
    # Priority queue example: processing tasks by priority
    print("\nPriority Queue Example:")
    tasks = [
        (5, "Send email"),
        (1, "Fix critical bug"),
        (3, "Review code"),
        (2, "Deploy application"),
        (4, "Update documentation")
    ]
    
    task_heap = MinHeap()
    for priority, task_name in tasks:
        task_heap.insert((priority, task_name))
        
    print("Processing tasks by priority:")
    while not task_heap.is_empty():
        priority, task = task_heap.extract_min()
        print(f"Processing: {task} (Priority: {priority})")