cipher = [115, 105, 103, 111, 112, 104, 122, 109, 131, 124, 82, 116, 114, 129, 63, 125, 119, 112, 104, 116, 128, 138, 73, 138, 149]
cipher = [cipher[i] - i for i in range(len(cipher))]
cipher = [chr(x) for x in cipher]

print ''.join(cipher)
