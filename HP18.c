//Problem Link :https://www.codechef.com/JAN19B/problems/HP18
#include<stdio.h>
#include<stdlib.h>
int main(){
	int t , a , b,flag = 0;
	scanf("%d",&t);
	long int n,i,c1 =0,c2=0;
	//long long int max = -1;
	while (t--){
		flag = 0;
		scanf("%ld",&n);
		scanf("%d",&a);
		scanf("%d",&b);
		long long int *arr = (long long int*)malloc(n*(sizeof(long long int)));
		for(i = 0; i < n; i++){
			scanf("%lld",arr+i);
			
			
	    			if(arr[i] % a == 0)
	    				c1 = c1+1;
	    			else if(arr[i] % b == 0)
	    				c2 = c2+1;
			    
			
		}
		if(c2 >= c1)
				printf("ALICE\n");
			else
				printf("BOB\n");
        	c1 = 0;
		c2 = 0;
		free(arr);
	
	}


	return 0;

}