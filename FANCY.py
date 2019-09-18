#Problem Link :https://www.codechef.com/JAN19B/problems/FANCY
import sys
t = int(input())
while t:
	l1 = [str(i) for i in input().split()]
	count = l1.count("not")
	if count > 0:
		print("Real Fancy")
	else:
		print("regularly fancy")
	t = t-1