#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include<stdbool.h>
#define LIMIT pow(10,10)

#include"../is_prime.c"


int main(void) {
  bool print = true;
  long long cand = 9, sq = 0;
  do {
    print = true;
    cand += 2;
    if(is_prime(cand)==true) continue;
    for(sq = 1; sq <= sqrt(cand/2); sq++) {
      if(is_prime(cand - 2*sq*sq)==true) {print = false; break;};
    };
    
    if(print == true) {
      printf("cand: %lld\n",cand);
      return 0;
    };

  } while(cand < LIMIT);

	return 1;
}

