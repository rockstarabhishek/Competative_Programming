//Problem Link :https://www.codechef.com/COOK103B/problems/TABLET
#include <stdio.h>

int main(void) {
	int t,n,w,h;
	long long int b,p,max = 0;
	scanf("%d",&t);
	while(t--){
	    max = 0;
	    scanf("%d %lld",&n,&b);
	    while(n--){
	        scanf("%d %d %lld",&w,&h,&p);
	        if(b>=p){
	            if((w*h) > max){
	                max = (w*h);
	            }
	         }
	        
	    }
	    if(max ==  0)
	        printf("no tablet\n");
	    else
	        printf("%lld\n",max);
	    
	}
	return 0;
}

