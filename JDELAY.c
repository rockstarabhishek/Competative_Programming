//Problem Link :https://www.codechef.com/LTIME64B/problems/JDELAY
#include<stdio.h>
#include<stdlib.h>
int main(){
	int t;
	int c = 0;
	int a,b,n;
	scanf("%d",&t);
	while(t--){
		scanf("%d",&n);
		while(n--){
			scanf("%d",&a);
			scanf("%d",&b);
			if((b-a) > 5)
				c++;
		}
		printf("%d\n",c);
		c = 0;
	}
	

	return 0; 
}