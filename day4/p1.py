#impure function:has side effects modifies external state
counter = 0

def increment_counter():
    global counter
    counter += 1
    return counter

def pure_increment(x):
    return x + 1
print(pure_increment(5))  # Output: 1
print(pure_increment(5))  # Output: 6