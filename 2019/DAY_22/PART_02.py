import sys, math, copy

length = 119315717514047
n = 101741582076661
card = 2020

incr = 1
offset = 0

file = open(sys.argv[1], 'r')
for line in reversed(list(file)):
	arg = line.strip().split()

	if arg[0] == "cut":
		val = int(arg[1])
		offset += val

	elif arg[2] == "new":
		incr *= -1
		offset += 1 # have shift by 1 before modding negative number (or else 0 will be double counted)
		offset *= -1
		
	elif arg[2] == "increment":
		val = int(arg[3])
		reverseMod = pow(val, length-2, length) #reverse mod of prime
		incr *= reverseMod
		offset *= reverseMod

	incr %= length
	offset %= length

file.close()

# Where a = incr and b = offset...
# f1(x) = ax + b
# f2(x) = a(ax + b) + b
#       = a^2x + ab + b
# f3(x) = a^2(ax + b) + ab + b
#       = a^3x + a^2b + ab + b
# ...
# fn(x) = a^nx + a^(n-1)b + a^(n-2)b + ... + b
#       = a^nx + b * sum of (a^n-1 + a^n-2 + ... + a^2 + a + 1)
#       = a^nx + b * (a^n - 1) / (a - 1)
#       = a^nx + b * (a^n - 1) * inv(a - 1, length)
pos = pow(incr, n, length) * card
pos += offset * (pow(incr, n, length) - 1) * (pow(incr-1, length - 2, length))
pos %= length

print("Card %i is in position %i" % (card, pos))