#Problem Link :https://www.codechef.com/FEB19B/problems/CHEFING
t = int(input())
while(t):
	i = int(input())
	l = []
	str = input()
	l.append(set(str))
	for j in range (1,i):
	    str = input()
	    l[0] = l[0].intersection(set(str))
	print(len(l[0]))
	t = t-1