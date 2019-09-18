//Problem Link :https://www.codechef.com/COOK102B/problems/ADASCOOL
#include <stdio.h>

int main(void) {
	int t,a,b;
	scanf("%d",&t);
	while(t--){
	    scanf("%d %d",&a,&b);
	    if((a) == 1 || (b) == 1)
	        printf("NO\n");
	    else if((a % 2) == 0 || (b % 2) == 0)
	        printf("YES\n");
	    else
	        printf("NO\n");
	    
	}
	return 0;
}

