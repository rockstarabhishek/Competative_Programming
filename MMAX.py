#Problem Link :https://www.codechef.com/JULY19B/problems/MMAX
# cook your dish here
for _ in range(int(input())):
    n = int(input())
    k = int(input())
    l = []
    if(k%n == 0):
        print('0')
    else:
        n1 = k%n
        n2 = n - k%n
        if(n1 == n2):
            print(2*(n1) - 1)
        else:
            if(n1 < n2):
                print(2*(n1))
            else:
                print(2*(n2))
"""        for i in range(n):
            l.append(k//n)
        for i in range(k%n):
            l[i] = l[i] + 1
        l1 = l[:k%n]
        l2 = l[k%n:]
        i = 0 
        j = 0
        l3 = []
        for k in range(len(l)):
            if(i < len(l1)):
                l3.append(l1[i])
                i = i + 1
            if(j < len(l2)):
                l3.append(l2[j])
                j = j + 1
        for i in range(len(l3)):"""
        