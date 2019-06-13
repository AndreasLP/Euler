#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include<stdbool.h>
int coin_val[8] = {200,100,50,20,10,5,2,1};
int coin_comb(int left, int idx){
	if(idx==7 || left==0) return 1;
	int sum_tot = 0;
	for(int nCoin = 0; nCoin <= left/coin_val[idx]; nCoin++){
		sum_tot += coin_comb(left-nCoin*coin_val[idx],idx+1);
	};
	return sum_tot;
};
int main(void) {
	printf("%d combs\n",coin_comb(200,0));
	return 0;
}

