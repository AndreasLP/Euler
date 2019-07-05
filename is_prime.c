
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>


bool is_prime(long long n){
  if(n < 2) return false;
  if(n < 4) return true;
  if(n%2==0 || n%3==0) return false;
  if(n < 15) return true;
  long long r = (long long)floor(sqrt(n)),f=5;

  for(; f <= r; f+= 6) {
    if(n%f==0) return false;
    if(n%(f+2)==0) return false;
    
  };

  return true;



};
/*
int main(int argc, char ** argv){
  long long pi_func = 1000; 
  if(argc == 2) pi_func = atol(argv[1]);
  //for(int n = 2; n <= pi_func; n++) if(is_prime((long long)n)==true) {
    //printf("%d\n",n);
  //  count++;
  //};
  //printf("Primes <= %d: %d\n",pi_func,count);
  printf("%d\n",is_prime(pi_func));
};
*/

