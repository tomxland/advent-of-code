import sys

y = int(sys.argv[1])
x = int(sys.argv[2])


def getBaseSum(n): 
	return n*(n+1)//2

def getIndex(row, col):
	return getBaseSum(row + col - 2) + col

start = getIndex(6,6)
end = getIndex(y,x)
val = 27995004

for i in range(start,end):
	val = val * 252533 % 33554393

print(val)