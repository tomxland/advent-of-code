def getCycles(banks):
    log = set()
    timesFound = 0

    counter = 0
    bankTarget = "" 

    while timesFound < 2:
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

        if timesFound == 0:
            if bankStr in log:
                bankTarget = bankStr
                timesFound = 1
                counter = 0
            else:
                log.add(bankStr)
        elif bankTarget == bankStr:
            timesFound = 2

    return counter

banks = [4,1,15,12,0,9,9,5,5,8,7,3,14,5,12,3]
print(getCycles(banks))