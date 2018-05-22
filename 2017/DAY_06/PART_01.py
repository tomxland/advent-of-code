def getCycles(banks):
    log = set()
    found = False

    counter = 0

    while not found:
        #Find max
        counter += 1

        maxIndex = 0
        maxValue = 0

        for index, b in enumerate(banks):
            if b > maxValue:
                maxValue = b
                maxIndex = index

        banks[maxIndex] = 0

        for i in range(maxValue):
            offset = (maxIndex + 1 + i) % len(banks)
            banks[offset] += 1

        bankStr = ','.join(str(b) for b in banks)

        if bankStr in log:
            found = True
        else:
            log.add(bankStr)
            print(counter,bankStr)

    return counter

banks = [4,1,15,12,0,9,9,5,5,8,7,3,14,5,12,3]
print(getCycles(banks))