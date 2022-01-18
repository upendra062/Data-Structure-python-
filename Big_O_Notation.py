"""Big O Notation = measuring time of the program in absolute term is not useful.
    It has to mathematically represented. That mathematically representation
    is Big-O-Notation
    This is an example of the time complexity of program of order n.
    time = a*n + b
    here b is removed.
    because we only have to keep the fastest growing term. and remove constant
    time = a*n
    so it time complexity order of n.
"""
# Keep the fasted growing term value of n2 or n
# drop the constant example b and bx + c

def get_squared_number(numbers):
    squared_numbers = []
    for n in numbers:
        squared_numbers.append(n*n)
    return squared_numbers

numbers = [2,5,8,9]
print(get_squared_number(numbers))

