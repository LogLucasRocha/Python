a = 1
b = 1
c = 0
s = 0

def sum_even_fibonacci(n):
  global a, b, s, c
  while c <= n:
    c = a + b
    if c % 2 == 0:
      s += c
    a = b
    b = c
  print(s)

sum_even_fibonacci(4000000)