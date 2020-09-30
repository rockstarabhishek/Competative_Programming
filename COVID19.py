#Codechef Problem Link --> https://www.codechef.com/MAY20B/problems/COVID19/

for _ in range(int(input())):
    num = int(input())
    dist = [int(i) for i in input().split()]
    infected = 1
    infected_list = []
    for i in range(1,num):
        if(dist[i] - dist[i - 1] < 3):
            infected = infected + 1
        else:
            infected_list.append(infected)
            infected = 1
    infected_list.append(infected)
    print(min(infected_list),end = " ")
    print(max(infected_list))
    