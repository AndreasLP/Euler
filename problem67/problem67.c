#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include<stdbool.h>
struct matrix{
size_t i,j;
long long** val;
};
typedef struct matrix matrix;
matrix* allocMatrix(size_t i, size_t j) {
	matrix* mat = malloc(sizeof(matrix));
	if(mat==NULL) return NULL;
	mat->i = i; mat->j = j;
	long long** rows = malloc(sizeof(long long*)*i);
	if(rows==NULL) {free(mat);return NULL;};
	long long* row_val = malloc(sizeof(long long)*i*j);
	if(row_val==NULL) {free(rows);free(mat);return NULL;};
	for(size_t row = 0; row < i; row++){
		rows[row] = row_val+j*row;
	};
	mat->val=rows;
	return mat;

};

void freeMat(matrix* mat) {
	free(*mat->val);
	free(mat->val);
	free(mat);
};

int main(void) {
	// File need a new line after the last line with numbers
	FILE* pfile = fopen("pyramid_large.txt","r");
	unsigned int lines=0;
    char tmp;	
	while(!feof(pfile)){
		//fscanf(pfile,"%d\n",&val);
		//printf("val: %d\n",val);
		tmp=fgetc(pfile);
		if(tmp=='\n') lines++; 
	};
	printf("lines: %d\n",lines);
	rewind(pfile);
	matrix* values = allocMatrix(lines,lines);
	for(size_t i = 0; i < lines; i++){
		for(size_t j = 0; j <= i; j++){
			fscanf(pfile,"%lld",*(values->val+i)+j);
		};
	};
	//for(size_t i = 0; i < lines; i++){for(size_t j = 0;j<=i;j++) printf("%2lli ",values->val[i][j]); printf("\n");};
	
	for(size_t i = 1; i < lines; i++){
		values->val[i][0]+=values->val[i-1][0];
		values->val[i][i]+=values->val[i-1][i-1];
		for(size_t j = 1;j<i;j++) {
			if(values->val[i-1][j-1] > values->val[i-1][j]) values->val[i][j] += values->val[i-1][j-1];
			else values->val[i][j] += values->val[i-1][j];
		};
	};
	
	//for(size_t i = 0; i < lines; i++){for(size_t j = 0;j<=i;j++) printf("%5lli ",values->val[i][j]); printf("\n");};
	
	long long max_val = 0;
	for(size_t j=0; j<lines; j++) if(values->val[lines-1][j]>max_val) max_val=values->val[lines-1][j];
	printf("Max: %llu\n",max_val);
	
	fclose(pfile);
	freeMat(values);
	return 0;
}

