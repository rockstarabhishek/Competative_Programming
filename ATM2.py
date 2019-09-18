#Problem Link :https://www.codechef.com/COOK98B/problems/ATM2
t = int(input())
while t :
	n,k = (input().split())
	s = ""
	l = input().split()
	for i in range (int(n)):
		if(int(k) >= int(l[i])):
			k = int(k) - int(l[i])
			s = s + '1'
		else:
			s = s + '0'
	print(s)
	t = t - 1