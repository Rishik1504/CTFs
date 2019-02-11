cipher = "5348454c4c4354465b5810527f41114f4e137f49157f561352597f5655114e1352604211455d"
cipher = cipher.decode('hex')
for i in range(256):
	msg = ''
	for j in cipher:
		msg += chr(ord(j)^i)
	if "shell" in msg:
		print msg