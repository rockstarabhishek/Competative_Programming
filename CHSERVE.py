#Problem Link :https://www.codechef.com/OCT18B/problems/CHSERVE
t = int(input())
l1 = []
while t:
	l1 = [int(i) for i in input().split()]
	if (int(((l1[0]+l1[1])/l1[2])%2) == 0):
		print('CHEF')
	else:
		print('COOK')
	t = t-1