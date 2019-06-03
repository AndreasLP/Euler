#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include<stdbool.h>
int isPrime(long long N){
	if(N%2==0) return false;
	for(long long test = 3; test <= sqrt(N); test+=2) if(N%test==0) return false;
	return true;
};


long long gcd(long long a, long long b){
	if(a==0||b==0) return 0;
	long long r=0;
	if(a<b) {r=a;a=b;b=r;};
	while(b!=0){
		r = a%b;
		a = b;
		b = r;
	}	
	return a;
};


int main(int argc, char** argv) {
	long long g=13LL,idx=5,end_point=(long long)pow(10,10); 
	if(argc==2) end_point = (long long) pow(10,atoi(argv[1]));
	printf("end point: %lli\n",end_point);

	for(long long gc,p; idx <= end_point; idx++) {
		gc = gcd(g,idx);	
		g += gc;
		if(gc > 1){
			p = g - (idx+1);
			if(isPrime(p)==true){
				if(p > end_point) {
					g=g+end_point-idx;
					idx=end_point;
					break;
				};
			idx = p;
			g = 3*p;
			};
		};
	};	
	
	printf("g(%llu)=%llu\n",idx,g);
	
	return 0;
}
