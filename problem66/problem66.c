#include<stdio.h>
#include<stdlib.h>
#include<math.h>
int diophantine_solver(const long double* D_arr,long double* x_sol,unsigned int* y_sol,const int idx){
  long double b = 1,D = D_arr[idx],a = (long double)round(sqrt(D));
  long double k = a*a-D,a_p,b_p,k_p;
  long double m=1,m_current=0,m_next=0;
  //printf("a: %d, b: %d, k: %d, D: %d, D_sqrt: %d\n",a,b,k,D,D_sqrt);
  while (k != 1){
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
    while(1==1){
      for(m_next=m_current+1;(fabs(k)-a%fabs(k))%fabs(k)!=(b*m_next)%fabs(k);m_next++) {
        //printf("%d ?= %d\n",(abs(k)-a%abs(k))%abs(k),(b*m_next)%abs(k));
      };
      //printf("%d ?? %d\n",abs(D-m_current*m_current),abs(D-m_next*m_next));
      if(fabs(D-m_current*m_current)>=fabs(D-m_next*m_next)) {m_current=m_next;}
      else break;
    }
    m = m_current;
    //printf("m: %d\n",m);
    //for(int i=1;i<1000000000;i++) printf("1\b");;
    a_p = a; b_p = b; k_p = k;
    a = (long double)(a_p*m+D*b_p)/fabs(k);
    b = (long double)(a_p + b_p*m)/fabs(k);
    k = (long double)(m*m - D)/(k_p);
    //printf("a: %d, b: %d, k: %d\n",a,b,k);
  };
  x_sol[idx]=abs(a);
  y_sol[idx]=abs(b);
	return 0;
	
};
int main(int argc, char **argv) {
  long double max_D = 1000,max_x=0,max_x_D=0;
  if(argc==2) max_D = atoi(argv[1]);
  long double n = max_D - (long double)sqrt(max_D);
  long double* D = malloc(sizeof(long double)*n);
  long double* x = malloc(sizeof(long double)*n);
  long double* y = malloc(sizeof(long double)*n);
  if(D==NULL||x==NULL||y==NULL) return -1;
  for(int idx=0,i=2, sqrt_i=0;i<=max_D;i++){
    sqrt_i = (int)sqrt(i);
    if(sqrt_i*sqrt_i!=i) {
      D[idx]=i;
      //printf("D[%d]=%d\n",idx,i);
      //diophantine_solver(D,x,y,idx);
      //if(0==diophantine_solver(D,x,y,idx)) printf("x: %7d D: %4d y:%d\n",x[idx],D[idx],y[idx]);
      //if(x[idx]>max_x) {
        //max_x=x[idx];
        //max_x_D=D[idx];
      //};
      idx++;
      };
      
    }; 
    int idx = 45;
    printf("D: %Lf\n",D[idx]);
    diophantine_solver(D,x,y,idx); 
    printf("x: %Lf y: %Lf\nD: %Lf\n",x[idx],y[idx],D[idx]);
 // for(int idx=0;idx<n;idx++) {
 //   printf("D[%d]=%d\n",idx,D[idx]);
 // };
  //printf("Max x: %d\n",max_x);
  //printf("D    : %d\n",max_x_D);
  free(D);
  free(x);
  free(y);
  return 0;
}
