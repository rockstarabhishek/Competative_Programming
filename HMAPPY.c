//Problem Link :https://www.codechef.com/FEB19B/problems/HMAPPY2
#include <stdio.h>

int main(void) {
	int t;
	long long int n,a,b,k,i,c;
	scanf("%d",&t);
	while(t--){
	    scanf("%lld %lld %lld %lld",&n,&a,&b,&k);
	    if( a == b){
	    	printf("Lose\n");
	    	continue;
	    }
	    else if((a%b) ==0 || (b%a) ==0 ){
	    	if(a>b){
	    		
	    		c=  (n/a) + (n/b) - 2*((n/b) / (a/b));
	    	}
	    	else{
	    		
	    		c=  (n/a) + (n/b) - 2*((n/a) / (b/a));
	    	}
	    	
	    }
	    else{
	    	c=  (n/a) + (n/b) -((n/a)/b) -((n/b)/a);
	    
	    }
	    if(c>=k)
	        printf("Win\n");
	    else
	        printf("Lose\n");
	    
	    
	}
	return 0;
}

