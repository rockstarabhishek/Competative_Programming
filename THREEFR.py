#Problem Link :https://www.codechef.com/LTIME65B/problems/THREEFR
t = int(input())
l = []
while(t):
	l1 = []
	l = [int (i) for i in input().split()]
	l1.append(l[0]+l[1]) 
	l1.append(l[0]+l[2]) 
	l1.append(l[2]+l[1])
	if l1[0] in l:
		print("yes")
	elif l1[1] in l:
		print("yes")
	elif l1[2] in l:
		print("yes")
	else :
		print("no")
	t = t - 1
	