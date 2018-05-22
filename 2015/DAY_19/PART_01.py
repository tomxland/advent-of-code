import re

string = "CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr"

replacements = {}
results = set()

file = open("input.txt",'r')

for line in file:
	args = re.split(r'\s[=>]*\s*',line.strip())
	key = args[0]
	if key not in replacements:
		replacements[key] = []

	replacements[key].append(args[1])

for key, valueList in replacements.items():
	index = 0
	while True:
		index = string.find(key, index)

		if (index == -1):
			break

		for value in valueList:

			newString = string[:index] + value + string[index+len(key):]
			results.add(newString)

		index += 1

print(len(results))