def dragonify(input, length):
	while len(input) < length:
		i = len(input) - 1
		input.append(False)

		while i >= 0:
			if input[i]:
				input.append(False)
			else:
				input.append(True)
			i -= 1

	return input[0:length]

def getChecksum(input):
	checksum = []
	i = 0
	while i < len(input):
		if input[i] == input[i+1]:
			checksum.append(True)
		else:
			checksum.append(False)

		i += 2

	if len(checksum) % 2 == 0:
		return getChecksum(checksum)

	else:
		return checksum

def toBoolArray(str):
	array = []
	for s in str:
		if s == "1":
			array.append(True)
		else:
			array.append(False)

	return array

def toString(array):
	str = ""
	for a in array:
		if a:
			str += "1"
		else:
			str += "0"
	return str

string = "10111100110001111"
input = toBoolArray(string)
toBoolArray(string)

length = 35651584
checksum = getChecksum(dragonify(input, length))
print(toString(checksum))

