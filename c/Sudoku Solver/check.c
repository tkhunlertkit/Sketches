/*
 *  check.c
 *  
 *
 *  Created by AraHana on 4/29/09.
 *  Copyright 2009 __MyCompanyName__. All rights reserved.
 *
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "check.h"
#include "global.h"
#include "variable.h"

int reader(char * name) {
	int i,j, tmp;
	char c[2];
	FILE *fp;
	
	/*strcpy(n, "sudoku.txt");
	strcat(n, name);
	
	printf("Destination of File = %s\n", n);
	*/
	
	fp = fopen(name, "r");
	if (fp == NULL) {
		return 1;
	}
	
	i=0;
	j=0;
	while ((tmp=fread(c, 1, 1, fp)) != 0) {
		c[tmp] = '\0';
		if (c[0] != '\n') {
			if ((tmp = atoi(c)) != 0) {
				ar[i][j].value = tmp;
			}
		}
		j++;
		if (c[0] == '\n') {
			i += 1;
			j = 0;
		}
	}
	fclose(fp);
	return 0;
}

void checkBlock(int startRow, int startCol) {
	int target;
	int i;
	int j;
	int k;
	int markCnt = 0;
	int markx, marky;
	
	for (target=1; target <=9; target++) {
		markCnt = 0;
		for (i=startRow; i<=startRow+2; i++) {
			for (j=startCol; j<=startCol+2; j++) {
				if (ar[i][j].value == 0) {
					for (k=0; k<ar[i][j].numCnt; k++) {
						if (ar[i][j].num[k] == target) {
							ar[i][j].mark = 1;
							markCnt += 1;
							markx = i;
							marky = j;
							break;
						}
					}
				}
			}
		}
		if (markCnt == 1) {
			ar[markx][marky].value = target;
			missing = 0;
			detect();
		}
		markCnt = 0;
	}
					
}

void checkRow() {
	int i, j, k, target;
	int markCnt = 0;
	int markx, marky;
	
	for (target=1; target<=9; target++) {
		markCnt = 0;
		for (i=0; i<9; i++) {
			for (j=0; j<9; j++) {
				if (ar[i][j].value == 0) {
					for (k=0; k<ar[i][j].numCnt; k++) {
						if (ar[i][j].num[k] == target) {
							markCnt += 1;
							markx = i;
							marky = j;
							break;
						}
					}
				}
				if (markCnt > 1) {
					break;
				}
			}
			if (markCnt == 1) {
				ar[markx][marky].value = target;
				missing = 0;
				detect();
			}
			markCnt = 0;
		}
	}
}

void checkCol() {
	int i, j, k, target;
	int markCnt = 0;
	int markx, marky;
	
	for (target=1; target<=9; target++) {
		markCnt = 0;
		for (i=0; i<9; i++) {
			for (j=0; j<9; j++) {
				if (ar[j][i].value == 0) {
					for (k=0; k<ar[j][i].numCnt; k++) {
						if (ar[j][i].num[k] == target) {
							markCnt += 1;
							markx = i;
							marky = j;
							break;
						}
					}
				}
				if (markCnt > 1) {
					break;
				}
			}
			if (markCnt == 1) {
				ar[marky][markx].value = target;
				missing = 0;
				detect();
			}
			markCnt = 0;
		}
	}
	
}

void checkSq() {
	int i; 
	int j;
	
	for (i=0; i<9; i++) {
		for (j=0; j<9; j++) {
			if (ar[i][j].numCnt == 1) {
				ar[i][j].value = ar[i][j].num[0];
				missing = 0;
				detect();
			}
		}
	}
}

void checkAll() {
	
	int i, j;
	int prevmis;
	int count=0;
	
	while (count <= 40) {
		for (i=0; i<3; i++) {
			for (j=0; j<3; j++) {
				prevmis = missing;
				checkBlock(i*3, j*3);
				if (prevmis != missing) {
					/*	printTbl();
					 //printf("////////////////////////////////////////////////////\n")
					 //getchar();;
					 */
					count = 0;
				}
			}
		}
		
		/* check each square */
		prevmis = missing;
		checkSq();
		if (prevmis != missing) {
			/*	printTbl();
			 printf("////////////////////////////////////////////////////\n");
			 getchar();
			 */
			count = 0;
		}
		
		/* check each row */
		prevmis = missing;
		checkRow();
		if (prevmis != missing) {
			/*	printTbl();
			 printf("////////////////////////////////////////////////////\n");
			 getchar();
			 */
			count = 0;
		}
		
		/* check each column */
		prevmis = missing;
		checkCol();
		if (prevmis != missing) {
			/*	printTbl();
			 printf("////////////////////////////////////////////////////\n");
			 getchar();
			 */
			count = 0;
		}
		count++;
	}
}	

void trer() {
	int done = 0;
	
	while (done == 0) {
		done = guessNum(0);
	}
	
	printf("Total Number of guess = %d\n", done);
	
}

void printTbl() {
	int i;
	int j;
	printf("\n");
	for (i=0; i<9; i++) {
		if (i==3 || i==6)
			printf("========================\n");
		
		for (j=0; j<9; j++) {
			if (j==3 || j==6)
				printf(" |");
			if (ar[i][j].value == 0)
				printf(" _");
			else
				printf(" %d", ar[i][j].value);
		}
		printf("\n");
	}
}

void detect() {
	int i, j;
	int k;
	int cannotbe[9];
	int counter;
	int canbe[9];
	
	for (i=0; i<9; i++) {
		for (j=0; j<9; j++) {
			if (ar[i][j].value == 0) {
				counter = cannotBe(i, j, cannotbe);
				counter = canBe(cannotbe, counter, canbe);
				for (k=0; k<counter; k++) {
					ar[i][j].num[k] = canbe[k];
				}
				ar[i][j].numCnt = counter;
				counter = 0;
				missing += 1;
			}
		}
		/* printf("i, j = %d, %d\n", i, j); */
	}
}

int cannotBe(int x, int y, int *cannotbe) {
	int l;
	int m;
	int k = 0;
	int found = 0;
	int startRow, startCol;
	int count;
	
	startRow = (x/3) * 3;
	startCol = (y/3) * 3;
	
	/* coloumn detection */
	for (m=0; m<9; m++) {
		if (ar[x][m].value != 0) {
			cannotbe[k] = ar[x][m].value;
			k++;
		}
	}
	
	/* row detection */
	for (l=0; l<9; l++) {
		if (ar[l][y].value != 0) {
			for (m=0; m<k; m++) {
				if (cannotbe[m] == ar[l][y].value) {
					found = 1;
					break;
				}
			}
			if (found == 0) {
				cannotbe[k] = ar[l][y].value;
				k++;
			}
		}
		found = 0;
	}
	
	/* block detection */
	for (l=startRow; l<=startRow+2; l++) {
		for (m=startCol; m<=startCol+2; m++) {
			if (ar[l][m].value != 0) {
				for (count=0; count<k; count++) {
					if (cannotbe[count] == ar[l][m].value) {
						found = 1;
						break;
					}
				}
				if (found == 0) {
					cannotbe[k] = ar[l][m].value;
					k++;
				}
			}
			found = 0;
		}
	}
	return k;
}

int canBe(int * cannotbe, int count, int *canbe) {
	int i, j;
	int k = 0;
	int dead = 0;
	
	for (i=1; i<=9; i++) {
		dead = 0;
		for (j=0; j<count; j++) {
			if (cannotbe[j] == i) {
				dead = 1;
				break;
			}
		}
		if (dead == 0) {
			canbe[k] = i;
			k++;
		}
	}
	return k;
}

void store(int x) {
	int i,j;
	
	for (i=0; i<9; i++)
		for (j=0; j<9; j++)
			tmpar[x][i][j] = ar[i][j];
		
}

void restore(int x) {
	int i,j;
	
	for (i=0; i<9; i++)
		for (j=0; j<9; j++)
			ar[i][j] = tmpar[x][i][j];
}

int guessNum(int x) {

	int i, j, k;
	int found = 0;
	int done = 0;
	
	/* printf("store at %d location\n", x); */
	store(x);
	for (i=0; i<9; i++) {
		for (j=0; j<9; j++) {
			if (ar[i][j].value == 0) {
				found = 1;
				break;
			}
		}
		if (found == 1)
			break;
	}
	
	for (k=0; k<ar[i][j].numCnt; k++) {
		/*
		printTbl();
		getchar();
		printf("resotoring x = %d\n", x);
		*/
		restore(x);
		ar[i][j].value = ar[i][j].num[k];
		missing = 0;
		detect();
		checkAll();
		if(missing == 0) {
			done = 1;
			return done;
		}
		if (done == 0) {
			done += guessNum(x+1);
		}
		if (done >= 1) {
			return done+1;
		}
			
		/* printf("x = %d\n", x); */
	}
	return done;
	
}