#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include<stdbool.h>

#define MAX 1000

unsigned long long mod_pow(unsigned long long b, unsigned long long e, unsigned long long n){
  unsigned long long val = 0;
  if(e>0) val=b%n;
  else return n>1 ? 1 : 0;
  for(size_t i=1; i<e; i++) val = (b*val)%n;
  return val;
};

int main(void) {
  unsigned long long n=pow(10,10),out=0;
  for(unsigned long long b=1; b <= MAX; b++) out = (out+mod_pow(b,b,n))%n;
  printf("Out: %llu\n",out);
	return 0;
}

