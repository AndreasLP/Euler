#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include<stdbool.h>
int main(void) {
	long long a=0,b=0,c=0;
	for(a=1;a<1000;a++) {
		for(b=1; b<1000; b++) {
			if(a+b<1000) c = 1000 - a - b;
			else continue;
			if(a*a+b*b==c*c) {
				printf("a: %lld, b: %lld, c: %lld\nabc: %lld\n",a,b,c,a*b*c);
				return 0;
			};
		};
	};
	return 1;
}
