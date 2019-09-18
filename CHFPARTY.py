#Problem Link :https://www.codechef.com/COOK103B/problems/CHFPARTY
# cook your dish here
t = int(input())
while(t):
    n = int(input())
    count = 0
    l  = [int(i) for i in input().split()]
    l.sort()
    for i in range(n):
        if(l[i] <= count):
            count = count + 1
    print(count)
    t = t -1