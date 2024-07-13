import string
import random

st = input("Enter the message : ")
words = st.split(" ")

x = input("Enter coding or decoding : ")

N = 3
ram1 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
ram2 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))

match x.lower():
	case "coding":
		nwords = []
		for word in words:
			if len(word) >= 3:
				stnew = ram1 + word[1:] + word[0] + ram2
				nwords.append(stnew)
			else:
				nwords.append(word[::-1])
		print(" ".join(nwords))
	case "decoding":
		nwords = []
		for word in words:
			if len(word) >= 3:
				stnew = word[3:-3]
				stnew = stnew[-1] + stnew[:-1]
				nwords.append(stnew)
			else:
				nwords.append(word[::-1])
		print(" ".join(nwords))
