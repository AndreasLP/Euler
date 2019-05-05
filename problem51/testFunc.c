#include "structures.h"

int_list* primes_to_n(int n);
void free_int_list(int_list* list);
bool isPrime(int n);

int main(void) {

  // int five[4][5] = {{1,0,0,0,1},
  //                   {0,1,0,0,1},
  //                   {0,0,1,0,1},
  //                   {0,0,0,1,1}};
  int six[10][6] = {{1,1,0,0,0,1},
                    {1,0,1,0,0,1},
                    {1,0,0,1,0,1},
                    {1,0,0,0,1,1},
                    {0,1,1,0,0,1},
                    {0,1,0,1,0,1},
                    {0,1,0,0,1,1},
                    {0,0,1,1,0,1},
                    {0,0,1,0,1,1},
                    {0,0,0,1,1,1}};
  // 1 fixed, 0 varies

  // int n = 100000;
  //
  // if(argc > 1){
  //   n = atoi(argv[1]);
  // }
  //
  // int_list* primes = primes_to_n(n);
  // if(primes==NULL)
  //   return -1;
  //


  // two fixed
  for (size_t f1 = 0; f1 < 10; f1++) {
    for (size_t f2 = 0; f2 < 10; f2++) {
      for (size_t f3 = 0; f3 < 10; f3++) {
        for (size_t i = 0; i < 10; i++) {
          int count = 0;
          for (size_t num = 0; num < 10; num++) {
            int cand = 0;
            int pot = 1;
            int fixed = f1;
            int second = 0;
            for (size_t k = 0; k < 6; k++) {
              if(six[i][0]==0 && num==0) continue;
              cand += (1-six[i][5-k])*num*pot+six[i][5-k]*fixed*pot;
              pot*=10;
              if(six[i][5-k]==1 && second==1){fixed = f3;second=2;};
              if(six[i][5-k]==1 && second==0){fixed = f2;second=1;};
            }
            if(isPrime(cand)==true) count += 1;
            if(cand == 121313) printf("Hit\n");
          }
          if(count==8){
            for (size_t num = 0; num < 10; num++) {
              int cand = 0;
              int pot = 1;
              int fixed = f1;
              int second = 0;
              for (size_t k = 0; k < 6; k++) {
                if(six[i][0]==0 && num==0) continue;
                cand += (1-six[i][5-k])*num*pot+six[i][5-k]*fixed*pot;
                pot*=10;
                if(six[i][5-k]==1 && second==1){fixed = f3;second=2;};
                if(six[i][5-k]==1 && second==0){fixed = f2;second=1;};
              }
              if(isPrime(cand)==true) {printf("Result is: %d\n", cand); return 0;};
            }
          }
        }
      }
    }
  }
  printf("Test 2\n");


  //free_int_list(primes);

  return 1;
}
