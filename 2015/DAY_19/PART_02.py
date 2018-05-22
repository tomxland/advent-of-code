import re
from queue import PriorityQueue

start = "CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr"

print(start.count("Ar"))

def findFewestSteps(start, target):
	q = PriorityQueue()
	q.put((len(start),0,start))

	while not q.empty():
		pair = q.get()
		string = pair[2]
		count = pair[1] + 1
		print(count)

		for key, valueList in replacements.items():
			index = 0

			while True:
				index = string.find(key, index)

				if (index == -1):
					break

				for value in valueList:

					newString = string[:index] + value + string[index+len(key):]
					
					if newString == target:
						return count

					q.put((len(newString), count,newString, ))

				index += 1

replacements = {}

file = open("input.txt",'r')

for line in file:
	args = re.split(r'\s[=>]*\s*',line.strip())
	val = args[0]
	key = args[1]

	if key not in replacements:
		replacements[key] = []

	replacements[key].append(val)

print(findFewestSteps(start,"e"))