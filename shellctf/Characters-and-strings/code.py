from Hidden.secret import flag

ct = []
for char in flag:
    ct.append(ord(char))

open('Characters-and-strings/params.txt','w').write(str(ct))
print(ct)