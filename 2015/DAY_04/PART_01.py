import hashlib

phrase = "ckczppom"

i = 1
while True:
	m = hashlib.md5()
	key = "%s%d" % (phrase, i)
	m.update(key.encode('utf-8'))
	digest = m.hexdigest()

	if digest.startswith("000000"):
		print(i)
		break
	else:
		i += 1