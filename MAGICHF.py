#Problem Link :https://www.codechef.com/SEPT18B/problems/MAGICHF
t = int(input())
while t:
	arr = input().split()
	tc  = []
	gold = int(arr[1])
	for i in range(int(arr[2])):
		tc.append(input().split())
		if (int(tc[i][0]) == gold):
			gold = int(tc[i][1])
		elif (int(tc[i][1]) == gold):
			gold = int(tc[i][0])
	print(gold)
	t = t - 1
	tc = []