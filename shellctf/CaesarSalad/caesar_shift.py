cipher = "furyypgs{fr3!_l0h_pna_u@px_gu1at5_g0b}"

from string import lowercase
all_letters = lowercase*2

for i in range(26):
	msg = ''
	for j in cipher:
		if j in all_letters:
			msg += all_letters[all_letters.index(j) + i]
		else:
			msg += j
	print msg