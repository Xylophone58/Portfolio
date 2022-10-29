numbers = [int(x) for x in input('Enter numbers:').split()]

# Return a list of only even numbers
odd_numbers = [x for x in numbers if (x % 2) != 0]
print('Even numbers only:', odd_numbers)