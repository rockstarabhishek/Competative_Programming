#Problem Link :https://www.codechef.com/JULY19B/problems/CHFM
# cook your dish here
for _ in range(int(input())):
    n = int(input())
    l = [int(i) for i in input().split()]
    s = sum(l)
    if(s%n == 0):
        if(l.count(s//n)):
            print(l.index(s//n)+1)
        else:
            print("Impossible")
    else:        
        print("Impossible")
        