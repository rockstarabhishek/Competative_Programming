#Problem Link :https://www.codechef.com/APRIL19B/problems/MAXREM
# cook your dish here
n = int(input())
l = set(map(int,input().split()))
l = list(l)
if(len(l) == 1):
    print("0")
else: 
    l.sort()
    print(l[len(l)-2]%l[len(l)-1])