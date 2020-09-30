#Codechef Problem Statement Link --> https://www.codechef.com/LTIME84B/problems/WWALK/

for _ in range(int(input())):
    n = int(input())
    A = [int(i) for i in input().strip().split()]
    B = [int(i) for i in input().strip().split()]
    weird  = 0
    sumA = 0
    sumB = 0
    for i in range (n):
        if (A[i] == B[i]):
            if(sumA == sumB):
                weird = weird + A[i]
        sumA += A[i]
        sumB += B[i]
    print(weird)