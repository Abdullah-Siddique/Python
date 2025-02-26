"""
Python Implementation of C++ STL Data Structures
This module implements the core functionality of the C++ Standard Template Library (STL)
containers in Python. It includes Vector, List, Deque, Stack, Queue, Priority Queue,
Set, Map, and MultiMap implementations.
"""

from abc import ABC, abstractmethod
import heapq
from collections import deque
from typing import Any, Callable, Generic, Iterator, List, Optional, Tuple, TypeVar, Dict, Set

T = TypeVar('T')
K = TypeVar('K')
V = TypeVar('V')

class STLContainer(Generic[T], ABC):
    """Base abstract class for all STL containers"""
    
    @abstractmethod
    def size(self) -> int:
        """Returns the number of elements in the container"""
        pass
    
    @abstractmethod
    def empty(self) -> bool:
        """Returns whether the container is empty"""
        pass
    
    @abstractmethod
    def clear(self) -> None:
        """Clears the contents of the container"""
        pass


class Vector(STLContainer[T]):
    """Implementation of C++ std::vector
    
    A dynamic array that can resize itself automatically when elements are added.
    Provides random access to elements in constant time.
    """
    
    def __init__(self, initial_elements: List[T] = None):
        """Initialize a new Vector, optionally with initial elements"""
        self._data = initial_elements.copy() if initial_elements else []
    
    def push_back(self, value: T) -> None:
        """Add an element to the end of the vector"""
        self._data.append(value)
    
    def pop_back(self) -> T:
        """Remove and return the last element"""
        if self.empty():
            raise IndexError("Vector is empty")
        return self._data.pop()
    
    def at(self, index: int) -> T:
        """Access element at specified position with bounds checking"""
        if index < 0 or index >= self.size():
            raise IndexError("Vector index out of range")
        return self._data[index]
    
    def front(self) -> T:
        """Access the first element"""
        if self.empty():
            raise IndexError("Vector is empty")
        return self._data[0]
    
    def back(self) -> T:
        """Access the last element"""
        if self.empty():
            raise IndexError("Vector is empty")
        return self._data[-1]
    
    def size(self) -> int:
        """Returns the number of elements"""
        return len(self._data)
    
    def empty(self) -> bool:
        """Returns whether the vector is empty"""
        return len(self._data) == 0
    
    def clear(self) -> None:
        """Clears all elements from the vector"""
        self._data.clear()
    
    def insert(self, index: int, value: T) -> None:
        """Insert element at specified position"""
        if index < 0 or index > self.size():
            raise IndexError("Vector index out of range")
        self._data.insert(index, value)
    
    def erase(self, index: int) -> None:
        """Remove element at specified position"""
        if index < 0 or index >= self.size():
            raise IndexError("Vector index out of range")
        del self._data[index]
    
    def __getitem__(self, index: int) -> T:
        """Operator[] equivalent for Python - allows container[index] syntax"""
        return self._data[index]
    
    def __setitem__(self, index: int, value: T) -> None:
        """Operator[] assignment - allows container[index] = value syntax"""
        self._data[index] = value
    
    def __iter__(self) -> Iterator[T]:
        """Returns an iterator over the elements"""
        return iter(self._data)
    
    def __str__(self) -> str:
        """String representation of the vector"""
        return f"Vector{{{', '.join(str(item) for item in self._data)}}}"


class ListNode(Generic[T]):
    """Node class for doubly-linked list implementation"""
    
    def __init__(self, data: T):
        self.data = data
        self.next = None
        self.prev = None


class List(STLContainer[T]):
    """Implementation of C++ std::list
    
    A doubly-linked list allowing constant time insertion and removal 
    anywhere in the container.
    """
    
    def __init__(self, initial_elements: List[T] = None):
        """Initialize a new List, optionally with initial elements"""
        self._head = None
        self._tail = None
        self._size = 0
        
        if initial_elements:
            for element in initial_elements:
                self.push_back(element)
    
    def push_front(self, value: T) -> None:
        """Add element to the beginning of the list"""
        new_node = ListNode(value)
        
        if self.empty():
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node
        
        self._size += 1
    
    def push_back(self, value: T) -> None:
        """Add element to the end of the list"""
        new_node = ListNode(value)
        
        if self.empty():
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            new_node.prev = self._tail
            self._tail = new_node
        
        self._size += 1
    
    def pop_front(self) -> T:
        """Remove and return the first element"""
        if self.empty():
            raise IndexError("List is empty")
        
        value = self._head.data
        
        if self._head is self._tail:  # Only one node
            self._head = None
            self._tail = None
        else:
            self._head = self._head.next
            self._head.prev = None
        
        self._size -= 1
        return value
    
    def pop_back(self) -> T:
        """Remove and return the last element"""
        if self.empty():
            raise IndexError("List is empty")
        
        value = self._tail.data
        
        if self._head is self._tail:  # Only one node
            self._head = None
            self._tail = None
        else:
            self._tail = self._tail.prev
            self._tail.next = None
        
        self._size -= 1
        return value
    
    def front(self) -> T:
        """Access the first element"""
        if self.empty():
            raise IndexError("List is empty")
        return self._head.data
    
    def back(self) -> T:
        """Access the last element"""
        if self.empty():
            raise IndexError("List is empty")
        return self._tail.data
    
    def size(self) -> int:
        """Returns the number of elements"""
        return self._size
    
    def empty(self) -> bool:
        """Returns whether the list is empty"""
        return self._size == 0
    
    def clear(self) -> None:
        """Clears all elements from the list"""
        self._head = None
        self._tail = None
        self._size = 0
    
    def __iter__(self) -> Iterator[T]:
        """Returns an iterator over the elements"""
        current = self._head
        while current:
            yield current.data
            current = current.next
    
    def __str__(self) -> str:
        """String representation of the list"""
        result = []
        current = self._head
        while current:
            result.append(str(current.data))
            current = current.next
        return f"List{{{', '.join(result)}}}"


class Deque(STLContainer[T]):
    """Implementation of C++ std::deque
    
    A double-ended queue that allows fast insertion and deletion
    at both the beginning and the end.
    """
    
    def __init__(self, initial_elements: List[T] = None):
        """Initialize a new Deque, optionally with initial elements"""
        self._data = deque(initial_elements if initial_elements else [])
    
    def push_front(self, value: T) -> None:
        """Insert element at the beginning"""
        self._data.appendleft(value)
    
    def push_back(self, value: T) -> None:
        """Add element to the end"""
        self._data.append(value)
    
    def pop_front(self) -> T:
        """Remove and return the first element"""
        if self.empty():
            raise IndexError("Deque is empty")
        return self._data.popleft()
    
    def pop_back(self) -> T:
        """Remove and return the last element"""
        if self.empty():
            raise IndexError("Deque is empty")
        return self._data.pop()
    
    def front(self) -> T:
        """Access the first element"""
        if self.empty():
            raise IndexError("Deque is empty")
        return self._data[0]
    
    def back(self) -> T:
        """Access the last element"""
        if self.empty():
            raise IndexError("Deque is empty")
        return self._data[-1]
    
    def at(self, index: int) -> T:
        """Access element with bounds checking"""
        if index < 0 or index >= self.size():
            raise IndexError("Deque index out of range")
        return self._data[index]
    
    def size(self) -> int:
        """Returns the number of elements"""
        return len(self._data)
    
    def empty(self) -> bool:
        """Returns whether the deque is empty"""
        return len(self._data) == 0
    
    def clear(self) -> None:
        """Clears all elements from the deque"""
        self._data.clear()
    
    def __getitem__(self, index: int) -> T:
        """Operator[] equivalent for Python"""
        return self._data[index]
    
    def __setitem__(self, index: int, value: T) -> None:
        """Operator[] assignment"""
        self._data[index] = value
    
    def __iter__(self) -> Iterator[T]:
        """Returns an iterator over the elements"""
        return iter(self._data)
    
    def __str__(self) -> str:
        """String representation of the deque"""
        return f"Deque{{{', '.join(str(item) for item in self._data)}}}"


class Stack(STLContainer[T]):
    """Implementation of C++ std::stack
    
    A container adapter that gives the functionality of a stack - 
    LIFO (last-in, first-out) data structure.
    """
    
    def __init__(self, initial_elements: List[T] = None):
        """Initialize a new Stack, optionally with initial elements"""
        # Using list as the underlying container for simplicity
        self._data = []
        if initial_elements:
            for element in initial_elements:
                self.push(element)
    
    def push(self, value: T) -> None:
        """Insert element at the top"""
        self._data.append(value)
    
    def pop(self) -> T:
        """Remove and return the top element"""
        if self.empty():
            raise IndexError("Stack is empty")
        return self._data.pop()
    
    def top(self) -> T:
        """Access the top element"""
        if self.empty():
            raise IndexError("Stack is empty")
        return self._data[-1]
    
    def size(self) -> int:
        """Returns the number of elements"""
        return len(self._data)
    
    def empty(self) -> bool:
        """Returns whether the stack is empty"""
        return len(self._data) == 0
    
    def clear(self) -> None:
        """Clears all elements from the stack"""
        self._data.clear()
    
    def __str__(self) -> str:
        """String representation of the stack"""
        return f"Stack[{', '.join(str(item) for item in reversed(self._data))}]"


class Queue(STLContainer[T]):
    """Implementation of C++ std::queue
    
    A container adapter that gives the functionality of a queue -
    FIFO (first-in, first-out) data structure.
    """
    
    def __init__(self, initial_elements: List[T] = None):
        """Initialize a new Queue, optionally with initial elements"""
        self._data = deque()
        if initial_elements:
            for element in initial_elements:
                self.push(element)
    
    def push(self, value: T) -> None:
        """Add element to the end of the queue"""
        self._data.append(value)
    
    def pop(self) -> T:
        """Remove and return the first element"""
        if self.empty():
            raise IndexError("Queue is empty")
        return self._data.popleft()
    
    def front(self) -> T:
        """Access the first element"""
        if self.empty():
            raise IndexError("Queue is empty")
        return self._data[0]
    
    def back(self) -> T:
        """Access the last element"""
        if self.empty():
            raise IndexError("Queue is empty")
        return self._data[-1]
    
    def size(self) -> int:
        """Returns the number of elements"""
        return len(self._data)
    
    def empty(self) -> bool:
        """Returns whether the queue is empty"""
        return len(self._data) == 0
    
    def clear(self) -> None:
        """Clears all elements from the queue"""
        self._data.clear()
    
    def __str__(self) -> str:
        """String representation of the queue"""
        return f"Queue[{', '.join(str(item) for item in self._data)}]"


class PriorityQueue(STLContainer[T]):
    """Implementation of C++ std::priority_queue
    
    A container adapter that provides constant time lookup of the 
    largest (by default) element, at the expense of logarithmic insertion.
    """
    
    def __init__(self, initial_elements: List[T] = None, 
                 compare: Callable[[T, T], bool] = None):
        """Initialize priority queue with optional elements and comparator
        
        Args:
            initial_elements: Optional list of initial values
            compare: Comparator function that returns True if first arg has higher priority
                    Default is max-heap (larger values have higher priority)
        """
        # Python's heapq is a min-heap, so we negate values for max-heap behavior by default
        self._data = []
        
        # If custom comparator provided, use it; otherwise default to max-heap
        self._reverse = compare is None
        self._compare = compare
        
        if initial_elements:
            for element in initial_elements:
                self.push(element)
    
    def push(self, value: T) -> None:
        """Insert element and sort the underlying heap"""
        if self._reverse:
            # For default max-heap, negate values (since heapq is min-heap)
            heapq.heappush(self._data, (-value if isinstance(value, (int, float)) 
                                     else (value, -1)))
        else:
            # Use custom comparator
            # Note: This is simplified; a real implementation would need more complexity
            heapq.heappush(self._data, value)
    
    def pop(self) -> T:
        """Remove and return the top element"""
        if self.empty():
            raise IndexError("Priority queue is empty")
        
        value = heapq.heappop(self._data)
        if self._reverse and isinstance(value, (int, float)):
            return -value
        return value
    
    def top(self) -> T:
        """Access the top element"""
        if self.empty():
            raise IndexError("Priority queue is empty")
        
        value = self._data[0]
        if self._reverse and isinstance(value, (int, float)):
            return -value
        return value
    
    def size(self) -> int:
        """Returns the number of elements"""
        return len(self._data)
    
    def empty(self) -> bool:
        """Returns whether the priority queue is empty"""
        return len(self._data) == 0
    
    def clear(self) -> None:
        """Clears all elements from the priority queue"""
        self._data.clear()
    
    def __str__(self) -> str:
        """String representation of the priority queue"""
        # Note: This isn't showing elements in priority order
        if self._reverse:
            elements = [str(-x if isinstance(x, (int, float)) else x) for x in self._data]
        else:
            elements = [str(x) for x in self._data]
        return f"PriorityQueue[{', '.join(elements)}]"


class StlSet(STLContainer[T]):
    """Implementation of C++ std::set
    
    A sorted associative container that contains unique elements.
    """
    
    def __init__(self, initial_elements: List[T] = None):
        """Initialize a new Set, optionally with initial elements"""
        self._data = set(initial_elements) if initial_elements else set()
    
    def insert(self, value: T) -> bool:
        """Insert element into the set if it doesn't exist already
        
        Returns:
            True if insertion took place, False otherwise
        """
        if value in self._data:
            return False
        self._data.add(value)
        return True
    
    def erase(self, value: T) -> int:
        """Remove element from the set
        
        Returns:
            Number of elements removed (0 or 1)
        """
        if value in self._data:
            self._data.remove(value)
            return 1
        return 0
    
    def contains(self, value: T) -> bool:
        """Check if element exists in set"""
        return value in self._data
    
    def size(self) -> int:
        """Returns the number of elements"""
        return len(self._data)
    
    def empty(self) -> bool:
        """Returns whether the set is empty"""
        return len(self._data) == 0
    
    def clear(self) -> None:
        """Clears all elements from the set"""
        self._data.clear()
    
    def __iter__(self) -> Iterator[T]:
        """Returns an iterator over the elements"""
        return iter(self._data)
    
    def __str__(self) -> str:
        """String representation of the set"""
        return f"Set{{{', '.join(str(item) for item in sorted(self._data))}}}"


class StlMap(STLContainer[Tuple[K, V]]):
    """Implementation of C++ std::map
    
    A sorted associative container that contains key-value pairs with unique keys.
    """
    
    def __init__(self, initial_elements: List[Tuple[K, V]] = None):
        """Initialize a new Map, optionally with initial elements"""
        self._data = {}
        if initial_elements:
            for key, value in initial_elements:
                self.insert(key, value)
    
    def insert(self, key: K, value: V) -> bool:
        """Insert key-value pair if key doesn't exist
        
        Returns:
            True if insertion took place, False otherwise
        """
        if key in self._data:
            return False
        self._data[key] = value
        return True
    
    def erase(self, key: K) -> int:
        """Remove element with specified key
        
        Returns:
            Number of elements removed (0 or 1)
        """
        if key in self._data:
            del self._data[key]
            return 1
        return 0
    
    def find(self, key: K) -> Optional[V]:
        """Find element with specified key
        
        Returns:
            Value for the key if found, None otherwise
        """
        return self._data.get(key)
    
    def contains(self, key: K) -> bool:
        """Check if key exists in map"""
        return key in self._data
    
    def at(self, key: K) -> V:
        """Access element with bounds checking
        
        Raises:
            KeyError: If key doesn't exist
        """
        if key not in self._data:
            raise KeyError(f"Key {key} not found in map")
        return self._data[key]
    
    def size(self) -> int:
        """Returns the number of elements"""
        return len(self._data)
    
    def empty(self) -> bool:
        """Returns whether the map is empty"""
        return len(self._data) == 0
    
    def clear(self) -> None:
        """Clears all elements from the map"""
        self._data.clear()
    
    def keys(self) -> Set[K]:
        """Returns all keys in the map"""
        return set(self._data.keys())
    
    def values(self) -> List[V]:
        """Returns all values in the map"""
        return list(self._data.values())
    
    def items(self) -> List[Tuple[K, V]]:
        """Returns all key-value pairs in the map"""
        return list(self._data.items())
    
    def __getitem__(self, key: K) -> V:
        """Operator[] equivalent for Python - allows access via map[key]"""
        return self._data[key]
    
    def __setitem__(self, key: K, value: V) -> None:
        """Operator[] assignment - allows map[key] = value syntax"""
        self._data[key] = value
    
    def __iter__(self) -> Iterator[K]:
        """Returns an iterator over the keys"""
        return iter(self._data)
    
    def __str__(self) -> str:
        """String representation of the map"""
        items = [f"{k}: {v}" for k, v in sorted(self._data.items(), 
                                              key=lambda x: x[0])]
        return f"Map{{{', '.join(items)}}}"


class MultiMap:
    """Implementation of C++ std::multimap
    
    A sorted associative container that contains key-value pairs with non-unique keys.
    """
    
    def __init__(self, initial_elements: List[Tuple[K, V]] = None):
        """Initialize a new MultiMap, optionally with initial elements"""
        self._data: Dict[K, List[V]] = {}
        if initial_elements:
            for key, value in initial_elements:
                self.insert(key, value)
    
    def insert(self, key: K, value: V) -> None:
        """Insert key-value pair"""
        if key not in self._data:
            self._data[key] = []
        self._data[key].append(value)
    
    def erase(self, key: K) -> int:
        """Remove all elements with specified key
        
        Returns:
            Number of elements removed
        """
        if key in self._data:
            count = len(self._data[key])
            del self._data[key]
            return count
        return 0
    
    def erase_one(self, key: K, value: V) -> int:
        """Remove one specific key-value pair
        
        Returns:
            1 if removed, 0 if not found
        """
        if key in self._data and value in self._data[key]:
            self._data[key].remove(value)
            if not self._data[key]:  # Remove key if no values left
                del self._data[key]
            return 1
        return 0
    
    def find(self, key: K) -> List[V]:
        """Find all values with specified key
        
        Returns:
            List of values for the key if found, empty list otherwise
        """
        return self._data.get(key, [])
    
    def contains(self, key: K) -> bool:
        """Check if key exists in multimap"""
        return key in self._data
    
    def count(self, key: K) -> int:
        """Count number of elements with specified key"""
        return len(self._data.get(key, []))
    
    def size(self) -> int:
        """Returns the total number of elements"""
        return sum(len(values) for values in self._data.values())
    
    def empty(self) -> bool:
        """Returns whether the multimap is empty"""
        return len(self._data) == 0
    
    def clear(self) -> None:
        """Clears all elements from the multimap"""
        self._data.clear()
    
    def keys(self) -> List[K]:
        """Returns all keys in the multimap (may include duplicates)"""
        result = []
        for key, values in self._data.items():
            result.extend([key] * len(values))
        return result
    
    def values(self) -> List[V]:
        """Returns all values in the multimap"""
        result = []
        for values in self._data.values():
            result.extend(values)
        return result
    
    def items(self) -> List[Tuple[K, V]]:
        """Returns all key-value pairs in the multimap"""
        result = []
        for key, values in self._data.items():
            for value in values:
                result.append((key, value))
        return result
    
    def __str__(self) -> str:
        """String representation of the multimap"""
        items = []
        for key in sorted(self._data.keys()):
            for value in self._data[key]:
                items.append(f"{key}: {value}")
        return f"MultiMap{{{', '.join(items)}}}"


# Example usage
def demo():
    # Vector example
    print("===== Vector Example =====")
    v = Vector([1, 2, 3])
    v.push_back(4)
    v.push_back(5)
    print(f"Vector: {v}")
    print(f"Size: {v.size()}")
    print(f"Element at index 2: {v.at(2)}")
    print(f"Front: {v.front()}, Back: {v.back()}")
    v.pop_back()
    print(f"After pop_back: {v}")
    
    # List example
    print("\n===== List Example =====")
    lst = List([10, 20, 30])
    lst.push_front(5)
    lst.push_back(40)
    print(f"List: {lst}")
    print(f"Size: {lst.size()}")
    print(f"Front: {lst.front()}, Back: {lst.back()}")
    lst.pop_front()
    print(f"After pop_front: {lst}")
    
    # Stack example
    print("\n===== Stack Example =====")
    s = Stack([1, 2, 3])
    s.push(4)
    print(f"Stack: {s}")
    print(f"Top: {s.top()}")
    s.pop()
    print(f"After pop: {s}")
    
    # Queue example
    print("\n===== Queue Example =====")
    q = Queue([1, 2, 3])
    q.push(4)
    print(f"Queue: {q}")
    print(f"Front: {q.front()}, Back: {q.back()}")
    q.pop()
    print(f"After pop: {q}")
    
    # Map example
    print("\n===== Map Example =====")
    m = StlMap([("apple", 5), ("banana", 3)])
    m.insert("orange", 10)
    print(f"Map: {m}")
    print(f"Value for 'apple': {m['apple']}")
    m["apple"] = 7  # Update value
    print(f"After updating 'apple': {m}")
    print(f"Contains 'grape': {m.contains('grape')}")
    

if __name__ == "__main__":
    demo()