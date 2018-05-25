import math

def isPrime(num):
  for i in range(2, int(math.sqrt(num)) + 1):
    if num % i == 0:
      return False

  return True

b = 67
h = 0

b *= 100
b += 100000
c = b + 17000


while b <= c:
  if not isPrime(b):
    h += 1
  b += 17

print(h)