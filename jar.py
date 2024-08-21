class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("It can't be negative")
        self._capacity = capacity
        self._size = 0
        

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if n > self._capacity:
            raise ValueError("More Cookies than the capacity")
        if self._size + n > self._capacity:
            raise ValueError("More Cookies than the capacity")
        self._size = self._size + n 
        

    def withdraw(self, n):
        if self._size < n:
            raise ValueError("Less Cookies than you can withdraw in the Jar")
        self._size = self._size -  n 
       
        
    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
        
        

