#include <iostream>

using namespace std;

int sum_num(int x) {
	int result = 0;
	int n = x;
	
	while(n != 0) {
		result += n % 10;
		n /= 10;
	}
	
	return result;
}

int main() {
	int n;
	cin >> n;
	
	int i = 1;
	int cnt = 0;
	for(i = 1; i <= n; i++) {
		if (i % sum_num(i) == 0) cnt++;
	}
	
	cout << cnt;
	return 0;
}
