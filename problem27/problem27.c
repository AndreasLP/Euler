#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include<stdbool.h>
bool isPrime(long long n){
  if(n<0) n*=-1;
  if(n<=2) return true;
  if(n%2==0) return false;
  for(long long i = 3; i <= sqrt(n); i+=2) if(n%i==0) return false;
  return true;
};

long long len_seq(long long a, long long b){
  long long len_neg = 1, len_pos = 1,n=-1;
  while(isPrime(n*n+a*n+b)) {n--;len_neg++;};
  n = 1;
  while(isPrime(n*n+a*n+b)) {n++;len_pos++;};
  if(len_neg > len_pos) return len_neg;
  else return len_pos;

};

int main(void) {
  long long limit = 1000, max_seq = 0, seq = 0, max_a = 0, max_b = 0;
  printf("test: %lli\n",len_seq(1,41));
  for(long long a = -limit; a <= limit; a++){
    for(long long b = -limit; b <= limit; b++){
      if(isPrime(b)==true){
        seq = len_seq(a,b);
        if(seq > max_seq) {max_seq = seq; max_a = a; max_b = b;};

      };
    };
  };
  printf("max seq: %lli\na: %lli\nb: %lli\nprod: %lli\n",max_seq,max_a,max_b,max_a*max_b);
	return 0;
}

