#Problem Link :https://www.codechef.com/MARCH19B/problems/CHNUM
# cook your dish here
for _ in range(int(input())):
    n = int(input())
    c = 0
    c1 = 0
    l = [int(i) for i in input().split()]
    for i in range (n):
        if(l[i] >= 0):
            c = c+1
        else:
            c1 = c1+1
    if(c1 == 0):
        print(c,end = " ")
        print(c)
    else:
        print(c,end = " ")
        print(c1)