#Problem Link :https://www.codechef.com/APRIL19B/problems/STRCH
# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s,ch = input().split()
    c = 0
    t = 0
    for i in range(n):
        if(s[i] == ch ):
            c = c + ((i+1) - t) + ((i+1) - t) * (n - (i + 1))
            t = i + 1
    print(c)    
