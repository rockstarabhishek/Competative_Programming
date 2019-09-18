#Problem Statement Link : https://www.codechef.com/ZCOPRAC/problems/ZCO14003
t = int(input())
l = []
for i in range (t):
	l.append(int(input()))
l.sort()
for i in range(t):
	l[i] = l[i] * (t-i)
print(max(l))
