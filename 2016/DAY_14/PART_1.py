import hashlib

salt = "qzyelonm"

hashes = []

index = 0
count = 0
lastKey = 0

def getHash(num):
	m = hashlib.md5()
	string = "%s%d" % (salt, num)
	m.update(string.encode('utf-8'))
	return m.hexdigest()

while count < 64:
	if len(hashes) == index:
		hashes.append(getHash(index))

	currHash = hashes[index]

	i = 0
	tripleFound = False
	while i <= len(currHash) - 3:
		if currHash[i] == currHash[i+1] == currHash[i+2]:
			tripleFound = True
			break
		i += 1

	if tripleFound:
		for j in range(999):
			lookAhead = index + 1 + j

			if len(hashes) == lookAhead:
				hashes.append(getHash(lookAhead))

			quint = ""
			for k in range(5):
				quint += currHash[i]

			if quint in hashes[lookAhead]:
				lastKey = index
				count += 1
				break

	index += 1

print(lastKey)


