#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<unistd.h>
#include<stdint.h>
#include<inttypes.h>
#include <wchar.h>
int diophantine_solver(long long D_in,unsigned long long* x_sol,unsigned long long* y_sol,const int idx){
  unsigned __int128 b = 1,a = (unsigned __int128)round(sqrt(D_in)),a_p,b_p,k_p,D=D_in;
  __int128 k = a*a-D;
  unsigned __int128 m=1,m_current=0,m_next=0,k_abs;
  //printf("a: %d, b: %d, k: %d, D: %d, D_sqrt: %d\n",a,b,k,D,D_sqrt);
  while (k != 1 && isnormal(a) && isnormal(b) && isnormal(k)){
    //if(D_sqrt >a%abs(k)){
      //t = (int)ceil(((float)D_sqrt-a%abs(k))/abs(k));
      //if(b>=1){
        //m_floor = abs(k)*t+a%abs(b);
        //m_ceil = abs(k)*(t+1)+a%abs(b);
      //}
      //else {
        //m_floor=abs(k)*t+abs(k)-a%abs(k);
        //m_ceil=abs(k)*(t+1)+abs(k)-a%abs(k);
      //};
      //printf("t: %d, m_floor: %d, m_ceil: %d\n",t,m_floor,m_ceil);
      //if(abs(m_floor*m_floor-D)<=abs(m_ceil*m_ceil-D)){m = m_floor;}
      //else {m = m_ceil;};
    //}
    //else {m = a%abs(k);};
    m_current = 0;
    if(k<0) k_abs = -k;
    else k_abs = k;
    while(1==1){
      for(m_next=m_current+1;(k_abs-a%k_abs)%k_abs!=(b*m_next)%k_abs;m_next++) {
        //printf("%d ?= %d\n",(abs(k)-a%abs(k))%abs(k),(b*m_next)%abs(k));
      };
      //printf("%d ?? %d\n",abs(D-m_current*m_current),abs(D-m_next*m_next));
      if(llabs((long long)D-(long long)(m_current*m_current))>=llabs((long long)D-(long long)(m_next*m_next))) {m_current=m_next;}
      else break;
    }
    m = m_current;
    printf("m: %lld\n",(long long)m);
    //for(int i=1;i<1000000000;i++) printf("1\b");;
    a_p = a; b_p = b; k_p = k;
    a = (unsigned __int128) m*((unsigned __int128)a_p/k_abs)+(D*((unsigned __int128)b_p/k_abs))+(m*(a_p%k_abs)+D*(b_p%k_abs))/k_abs;
    //a = (unsigned __int128) (m*a_p+D*b)/k_abs;
    //printf("first: %lld, second: %lld\n",m*((unsigned __int128)a_p/k_abs),(m*(a_p%k_abs)+D*b_p)/k_abs);
    b = (unsigned __int128)(a_p/k_abs + (a_p%k_abs+ b_p*m)/k_abs);
    k = ((__int128)(m*m - D))/(k);
    printf("a: %lld, b: %lld, k: %lld\n",(unsigned long long)a,(unsigned long long)b,(long long)k);
  };
  x_sol[idx]=a;
  y_sol[idx]=b;
	return 0;

};
int main(int argc, char **argv) {
  FILE* x_file = fopen("D_x_list.txt","r");
  FILE* y_file = fopen("D_y_list.txt","r");


  //unsigned long long max_x=0,max_x_D=0;
  int max_D = 70;
  if(argc==2) max_D = atoi(argv[1]);
  long long n = max_D - (long long)sqrt(max_D);
  long long* D = malloc(sizeof(long long)*n);
  unsigned long long* x = malloc(sizeof(unsigned long long)*n);
  unsigned long long* y = malloc(sizeof(unsigned long long)*n);
  unsigned long long* x_true = malloc(sizeof(unsigned long long)*n);
  unsigned long long* y_true = malloc(sizeof(unsigned long long)*n);
  if(D==NULL||x==NULL||y==NULL||x_true==NULL||y_true==NULL||x_file==NULL||y_file==NULL) return -1;
  long long dump = 0;
  for (long long i = 0; i < n; i++) {
    fscanf(x_file,"%lld %lld",&dump,x_true+i);
    fscanf(y_file,"%lld %lld",&dump,y_true+i);
  }



  // for (size_t i = 0; i < n; i++) {
  //   printf("%zu: %lld %lld\n",i+1,x_true[i],y_true[i]);
  // }


  /*
  for(int idx=0,i=2, sqrt_i=0;i<=max_D;i++){
    sqrt_i = (int)sqrt(i);
    if(sqrt_i*sqrt_i!=i) {
      D[idx]=i;
      printf("D: %lld\n",D[idx]);
      diophantine_solver(D[idx],x,y,idx);
      //if(0==diophantine_solver(D[idx],x,y,idx)) printf("x: %7d D: %4d y:%d\n",x[idx],D[idx],y[idx]);
      if(x[idx]>max_x) {
        max_x=x[idx];
        max_x_D=D[idx];
      };
      idx++;
      };
    };
    */


    long long D_test = 571;
    int idx = 0;
    printf("D: %lld\n",D_test);
    diophantine_solver(D_test,x,y,idx);
    printf("x: %lld y: %lld\nD: %lld\n",x[idx],y[idx],D_test);


    /*
    for (long long i = 0; i < n; i++) {
      if(x_true[i]!=x[i] || y_true[i]!=y[i]) printf("D: %lld, x_true: %lld, x: %lld, y_true: %lld, y: %lld\n", D[i], x_true[i], x[i], y_true[i], y[i]);
    }
    */

 // for(int idx=0;idx<n;idx++) {
 //   printf("D[%d]=%d\n",idx,D[idx]);
 // };
  // printf("Max x: %lld\n",max_x);
  // printf("D    : %lld\n",max_x_D);
  free(D);
  free(x);
  free(y);
  free(x_true);
  free(y_true);
  fclose(x_file);
  fclose(y_file);
  return 0;
}
