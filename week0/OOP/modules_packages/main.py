# main.py

# Method 1: Import the whole module
import math_utils
print(math_utils.add(5, 3))      # 8
print(math_utils.pi)             # 3.14159

# Method 2: Import specific functions
from math_utils import square
print(square(4))                 # 16

# Method 3: Import with an alias
import math_utils as mu
print(mu.add(10, 20))            # 30

# Method 4: Import everything (⚠️ usually bad practice)
from math_utils import *
print(pi)                        # 3.14159
