#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include<stdbool.h>
long long num_factors_p12(long long N) {
//printf("N: %lli\n",N);
long long factors = 1,count=0;
if(N%2==0) N=N/2;
while(N%2==0) {N=N/2;count++;};
factors *= count+1;
long long div = 3;
//printf("N: %lli\n",N);
while(N!=1) {
	count = 0;
	while(N%div==0) {N=N/div;count++;};
	//printf("N: %lli\n",N);
	factors *= count+1;
	div+=2;
};
//printf("N: %lli\n",N);
return factors;
};

int main(int argc, char ** argv) {
	long long n_factors = 5;
	if(argc==2) n_factors = atoi(argv[1]);
	long long n = 1,l_num=num_factors_p12(n),r_num=num_factors_p12(n+1);
	while(l_num*r_num<n_factors) {
		//if(n%1==0) printf("\nn: %lli\nl: %lli r: %lli\n",n,l_num,r_num);
		n++;
		l_num=r_num;
		r_num=num_factors_p12(n+1);
	};
	printf("Triangular number %lli: %lli\n",n,(n*(n+1))/2);
	return 0;
}
