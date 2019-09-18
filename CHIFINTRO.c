//Problem Link :https://www.codechef.com/DEC18B/problems/CHFINTRO
#include<stdio.h>
int main(){
	int n,r;
	int R;
	scanf ("%d %d",&n,&r);
	while(n--){
		scanf("%d",&R);
		if(R >= r)
			printf("Good boi\n");
		else
			printf("Bad boi\n");
	}
	return 0;

}