#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <time.h>

int N;
int BITS; // 2^N
int count;

#define match(a, b) (bitcount[a^b])

/*
int match(int a, int b)
{
	int i, count = 0;
	for (i = 0; i < N; i++) {
		if ((a&1) == (b&1)) count++;
		a >>= 1; b >>= 1;
	}
	return count;
}
*/

int possible[33554432];
char bitcount[33554432];

//char guessresult[65536][65536];

void initguesses()
{
	int i, j, count;
	for (i = 0; i < BITS; i++) {
		j = i;
		count = 0;
		while (j) {if (j&1) count++; j>>=1;}
		bitcount[i] = N-count;
	}
	return;
}



void init()
{
	int i;
	for (i = 0; i < BITS; i++) possible[i] = i;
	count = BITS;
}

void binaryprint(int i)
{
	int j;
	for (j = N-1; j >= 0; j--)
		if (((i>>j)&1) == 1) printf("1");
		else printf("0");
	printf("\n");
}

int makeguess(int target) // returns 1 when we've got the answer
{
	int i,j, res, base = 0, guess;
	
	if (1) { // we guess possible[0]
		guess = possible[0];
		res = match(guess,target);
		for (j = 0; j < count; j++) {
			if (match(guess,possible[j]) == res) {
				possible[base++] = possible[j];
			}
		}
	}
	count = base;
	for (i = 0; i < count; i++)
		if (possible[i] != target) return 0;
	return 1;
}

int main()
{
	int i, j, target, step, total=0, maxstep;
	
	//srandomdev();
	for (N = 1; N < 26; N++) {
		total = 0;
		BITS = 1;
		maxstep = 0;
		for (i = 0; i < N; i++) BITS *= 2;
		initguesses();
		for (target = 0; target < BITS; target++) {
			step = 1;
			//binaryprint(target); printf("----------\n");
			init();
			while(1) {
				//printf("%2d: ", step++);
				step++;
				if (makeguess(target) != 0) break;
			}
			total += step-1;
			if (step-1 > maxstep) maxstep = step-1;
			//printf("\n");
		}
		printf("total: %d; num: %d, av: %g, max: %d\n", total, BITS, (float)total/(float)BITS, maxstep);
	}
	return 1;
}