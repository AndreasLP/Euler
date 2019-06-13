#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include<stdbool.h>
size_t count(size_t p){
	size_t cnt = 0;
	for(size_t a = 1,b,c; a <= p/2+1; a++){
		for(b=1; b<=a; b++){
			c=p-a-b;
			if(c*c==(a*a+b*b)) cnt++;
		};

	};
	return cnt;
};


int main(void) {
	size_t max_p=0,max_cnt=0;
	for(size_t p=2,count_val; p<=1000; p+=2){
		count_val = count(p);
		if(count_val>max_cnt) {max_cnt=count_val;max_p=p;};
	};
	printf("p: %zu\n",max_p);
	return 0;
}

