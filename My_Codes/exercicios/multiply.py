#encoding: utf-8

#fatorial
a = [1, 2, 3, 4, 5]

def multiply(numbers):
  total = 1
  for i in numbers:
    total *= i
  print(total)

multiply(a)
  