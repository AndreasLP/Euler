#ifndef stdio
#include <stdio.h>
#define stdio
#endif
#ifndef math
#include <math.h>
#define math
#endif
#ifndef stdlib
#include <stdlib.h>
#define stdlib
#endif
#ifndef stdbool
#include <stdbool.h>
#define stdbool
#endif


#ifndef structures
typedef struct int_list {
  unsigned long n;   /* length of vector                     */
  int * list;        /* pointer to array of length n         */
} int_list;

#define structures

#endif
