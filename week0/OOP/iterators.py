'''_iter__(): Returns the iterator object itself.

__next__(): Returns the next value. Raises StopIteration when done
'''

class Counter:
    def __init__(self, max):
        self.max = max
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.max:
            raise StopIteration  # Tells the loop to stop
        self.current += 1
        return self.current

# Using our custom iterator
for num in Counter(3):
    print(num)  # 1, 2, 3
