

def dragonify(input, length):
	while len(input) < length:
		b = ""
		for a in input:
			if (a == '1'):
				b = '0' + b
			else:
				b = '1' + b

		input += ('0' + b)
		print(input)

	return input[0:length]

def getChecksum(input):
	checksum = ""
	i = 0
	while i < len(input):
		if input[i] == input[i+1]:
			checksum += '1'
		else:
			checksum += '0'

		i += 2

	if len(checksum) % 2 == 0:
		return getChecksum(checksum)

	else:
		return checksum


string = "10111100110001111"
length = 272
print(getChecksum(dragonify(string, length)))
