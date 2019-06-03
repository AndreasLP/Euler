#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include<stdbool.h>
#define N 20
int main(void) {
	unsigned long long grid[N+1][N+1] = {};
	for(size_t i = 0; i <= N; i++) {grid[i][N]=1;grid[N][i]=1;};
	//for(int i = 0; i <= N; i++){for(int j = 0; j <= N; j++) {printf("%lli ",grid[i][j]);};printf("\n");};
	for(int i = N-1; i >= 0; i--) for(int j = N-1; j >= 0; j--) {grid[i][j]=grid[i+1][j]+grid[i][j+1];};
	//for(int i = 0; i <= N; i++){for(int j = 0; j <= N; j++) {printf("%9lli ",grid[i][j]);};printf("\n");};
	printf("test2\n");
	printf("%lli %lli\n",grid[0][1]+grid[1][0],grid[0][0]);
	return 0;
}

