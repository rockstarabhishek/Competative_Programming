#Problem Link :https://www.codechef.com/OCT18B/problems/BITOBYT
t = int(input())
bit = 0
nibble = 0
byte = 0
while t:
	n = int(input())
	if (int(n%26) == 0):
		byte = int(pow(2,int(n/26)-1))	
		print(bit,nibble,byte)
	else:
		if (int(n%26) > 10):
			byte = int(pow(2,int(n/26)))
			print(bit,nibble,byte)
		elif(int(n%26) > 2):
			nibble = int(pow(2,int(n/26)))
			print(bit,nibble,byte)
		else:
			bit = int(pow(2,int(n/26)))
			print(bit,nibble,byte)
	bit = 0
	nibble = 0
	byte = 0
	t = t-1