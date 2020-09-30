#Codechef Problem Statement Link --> https://www.codechef.com/LTIME84B/problems/LOSTWKND/

for _ in range(int(input())):
    week = [int(i) for i in input().strip().split()]
    weekday = week[:5]
    p = week[5]
    newweek = [i * p for i in weekday]
    if(sum(newweek) > 120):
        print("Yes")
    else:
        print("No")