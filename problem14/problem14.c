#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include<stdbool.h>
long long Collatz(long long N) {
	long long count = 0;
	while(N!=1) {
	if(N%2==0) N = N/2;
	else N = 3*N+1;
	count++;
	}
	return count;
};

int main(void) {
	long long max_count=0,current=0,max_N=0;
	for(long long N = 3; N <= pow(10,6); N++) {
		current = Collatz(N);
		if(current>max_count) {max_N=N;max_count=current;};
	};
	printf("N: %lli\nLength: %lli\n",max_N,max_count);
	return 0;
}

