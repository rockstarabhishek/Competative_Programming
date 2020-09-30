#Codechef Problem Statement Link --> https://www.codechef.com/LTIME84B/problems/LOSTWKND/

for _ in range(int(input())):
    Q,c = [int(i) for i in input().split()]
    que = input()
    dic = {}
    for char in que:
        if char in dic:
            dic[char] = dic[char] + 1
        else:
            dic[char] = 1
    for i in range(c):
        num = int(input())
        pending = 0
        for char in dic:
            if (num < dic[char]):
                pending = pending + dic[char] - num
        print(pending)
    

