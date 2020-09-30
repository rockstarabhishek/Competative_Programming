#Codechef Problem Statement Link --> https://www.codechef.com/SEPT20B/problems/TREE2/

for _ in range(int(input())):
    n = int(input())
    stick = [int(i) for i in input().split()]
    set_stick = set(stick)
    len_set_stick = len(set_stick)
    if(0 in set_stick):
        print(len_set_stick - 1)
    else:
        print(len_set_stick)
    # print(3)