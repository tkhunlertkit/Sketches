/*
 *  main.c
 *  
 *
 *  Created by AraHana on 4/29/09.
 *  Copyright 2009 __MyCompanyName__. All rights reserved.
 *
 */

#include <stdio.h>
#include <unistd.h>
#include "global.h"
#include "check.h"
#include "variable.h"


int main(int argc, char **argv) {
	/* int x, y; */
	int i, j;
	int tmp;
	char *string;
	
	missing = 0;
	for (i=0; i<9; i++) {
		for (j=0; j<9; j++) {
			ar[i][j].mark = 0;
			ar[i][j].numCnt = 0;
			ar[i][j].value = 0;
		}
	}
	
	if (argc == 1)
		string = "Sudoku.txt";
	else string = argv[1];
	
	tmp = reader(string);
	if (tmp == 1) {
		printf("File not found.. \n");
		printf("no %s in folder.\n", string);
		return 1;
	}
	
	detect();
	
	printTbl();
	printf("////////////////////////////////////////////////////\n");

	checkAll();
	
	
	if (missing != 0) {
		
		printf("Before Trial and error: \n");
		printTbl();
		printf("///////////////////////////////////////////////////\n");
		/*
		getchar();
		*/
		printf("trial and error mode...   T__T\n");
		trer();
	}
	/*
	x = 8;
	y = 1;
	printf("num[%d][%d].num = ", x, y);
	for (i=0; i<ar[x][y].numCnt; i++) {
		printf("%d, ", ar[x][y].num[i]);
	}
	printf ("\ncnt = %d\n", ar[x][y].numCnt);
	*/
	
	printTbl();
	
	if (missing == 0) 
		printf("\ncomplete solving   ^__^\n");
	else {
		printf("\n cannot solve.. T__T\n");
		printf("with number of missing positon of %d\n",missing);
	}

	return 0;
}