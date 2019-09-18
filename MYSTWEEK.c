//Problem Link :https://www.codechef.com/COAT2018/problems/MYSTWEEK
#include<stdio.h>
#include<stdlib.h>
int main(){
	int t,n,x;
	int i, sum = 0;
	int *arr;
	scanf("%d",&t);
	while(t){
		scanf("%d",&n);
		scanf("%d",&x);
		arr = (int *)malloc(sizeof(int) * n);
		for(i = 0; i < n; i++)
			scanf("%d",&(arr[i]));
		for(i = 0; i < n; i++){
			sum = sum + arr[i];
			if(sum == x || sum > x){
				printf("%d\n",i+1);
				break;
			}
			if(i == (n-1))
				i = -1;
		}
		sum = 0;
		t--;
		free(arr);
	}
	return 0;

}