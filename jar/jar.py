class Jar:
    def __init__(self,capacity=12):
        
        if not isinstance(capacity, int) or capacity <= 0 or capacity > 12:
            raise ValueError("Capacity must be a positive integer less than or equal to 12.")
        
        self._capacity = 12
        self._size = 0
    
        
    def __str__(self):
        return "🍪" * self._size

    def deposit(self,n):
        self._size+=n
        
        if self._size>self._capacity:
            raise ValueError("Cannot deposit more cookies than the jar's capacity.")
        
    def withdraw(self,n):
        self._size-=n
        
        if self._size<0:
            raise ValueError("Cannot withdraw more cookies than the jar contains.")
    
    @property
    def capacity(self):
        return self._capacity
    
    @property
    def size(self):
        return self._size

def main():
    
    jar = Jar()
    jar.deposit(10)
    print(jar)
    jar.withdraw(2)
    print(jar)  
    
if __name__ == "__main__":
    main()