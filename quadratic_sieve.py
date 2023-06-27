import math


n = 407

next_square = pow(math.ceil(math.sqrt(n)), 2)
next_square_root = math.sqrt(next_square)

while not (math.sqrt(pow(next_square_root, 2) - n)).is_integer():
    next_square_root += 1
    next_square = pow(next_square_root, 2)
    
print(f"n = {n}\np = {(int)(next_square_root)}\nq = {(int)(math.sqrt(next_square - n))}")