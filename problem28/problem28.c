#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include<stdbool.h>
 
int main(int argc, char ** argv) {
  unsigned long long Sn = 1, Pn = 1,size=2;
  if(argc==2) size = atoi(argv[1]);
  for(unsigned long long n = 1; n <= size; n++){
    Sn += 4*Pn+20*n;
    Pn += 8*n;
  };
  printf("Sum: %llu\n",Sn);
	return 0;
}

