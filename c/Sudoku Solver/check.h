/*
 *  check.h
 *  
 *
 *  Created by AraHana on 4/29/09.
 *  Copyright 2009 __MyCompanyName__. All rights reserved.
 *
 */

int reader(char *name);
void checkBlock(int startRow, int startCol);
void checkSq();
void checkRow();
void checkCol();
void checkAll();
void trer();
void store(int x);
void restore(int x);
void printTbl();
int cannotBe(int x, int y, int *cannotbe);
int canBe(int *cannotbe, int count, int *canbe);
void detect();
int guessNum(int x);