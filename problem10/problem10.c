#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include<stdbool.h>
bool isPrime(long long N){
	if(N%2==0) return false;
	for(long long test = 3; test<=sqrt(N); test+=2) if(N%test==0) return false;
	return true;
};
int main(int argc, char ** argv) {
	long long sum_val = 0,N=10;
	if(argc==2) N = atoi(argv[1]);
	if(N<2) sum_val = 0;
	else if(N==2) sum_val = 2;
	else {sum_val=2;for (long long num = 3; num <= N; num+= 2) if(isPrime(num)==true) sum_val+=num;};
	printf("Sum of primes less than %lli: %lli\n",N,sum_val);
	return 0;
}
