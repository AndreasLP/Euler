#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include<stdbool.h>
int main(void) {
	int day = 1,year = 1901,sundays=0;
	for(;year<=2000;year++){
		for(int month = 1; month <= 12; month++){
			if(month == 9 || month == 4 || month == 6 || month == 11) day = (day+30)%7;
			else if(month == 2 && year%4==0) day=(day+29)%7;
			else if(month == 2 && year%4!=0) day=(day+28)%7;
			else day=(day+31)%7;	
			if(day==6) sundays++;
		};
	};
	printf("Sundays: %d\n",sundays);
	return 0;
}

