#include <stdio.h>

int main() {
	int N, K;
	int Ks[100001];
	int i;
	
	scanf("%d %d", &N, &K);
	
	N -= (K + 1) * K / 2;
	
	if(N < 0) printf("%d", -1);
	else {
		if(!(N % K)) printf("%d", K-1);
		else printf("%d", K);
	}
	
	return 0;
	
}
