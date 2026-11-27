def count_up_to(max):
    num = 1
    while num <= max:
        yield num      # Pauses here, returns num, waits for next call
        num += 1

for n in count_up_to(3):
    print(n)  # 1, 2, 3

# List: Memory heavy
squares_list = [x**2 for x in range(100000000)]  # 💥 Crashes RAM

# Generator: Memory light
squares_gen = (x**2 for x in range(100000000))   # ⚡ Uses almost 0 MB
