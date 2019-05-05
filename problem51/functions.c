#include "structures.h"

#ifndef functions
#define functions

bool isPrime(int n){
    if(n<2) return false;
    if(n==2 || n==3) return true;
    if(n%2==0 || n%3==0) return false;
    if(n<9) return true;
    for(size_t i = 5; i < sqrt((double) n) +1 ; i+=6){
      if(n%i==0 || n%(i+2)==0) return false;
    }
    return true;
}
void free_int_list(int_list * list){
  if(list==NULL)
    return;

  free(list->list);
  free(list);

  return;
}

int_list* primes_to_n(size_t n) {
  // 1 not prime. 0 prime
  int* primes = calloc(n, sizeof(int));
  if(primes == NULL)
    return NULL;
  primes[0] = 1;
  size_t found_primes = 0;
  for(size_t pot_prime = 2; pot_prime <= n; pot_prime++){
    if(primes[pot_prime-1] == 0){
      for (size_t i = 2; i < n/pot_prime+1; i++) {
        primes[pot_prime*i-1] = 1;
      }
      found_primes++;
    }
  }

  int* primes_to_return = calloc(found_primes, sizeof(int));
  if(primes_to_return == NULL)
    return NULL;

  int prime = 1;
  for (size_t i = 0; i < found_primes; i++) {
    while(primes[prime-1]==1)
      prime++;
    primes_to_return[i] = prime++;
  }

  int_list* return_val = malloc(sizeof(int_list));
  if(return_val==NULL)
    return NULL;

  return_val->n = found_primes;
  return_val->list = primes_to_return;

  free(primes);

  return return_val;
}
#endif
