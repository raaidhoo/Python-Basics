# initial list:
single_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#list created by appending the loop value
squares = []
#list comprehension
cubes = [cube **3 for cube in single_digits]
#loop
for digits in single_digits:
  squares.append(digits**2)
  print(digits)
#output
print(squares)
print(cubes)