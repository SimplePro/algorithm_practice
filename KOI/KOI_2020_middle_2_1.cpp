#include <iostream>

using namespace std;

int solution(int A, int B, int C, int student) {
    int i, j, k;
    
    for(i=0; i <= student; i += A) {
        for(j = 0; j <= student; j += B) {
            for(k = 0; k <= student; k += C) {
                if(i + j + k == student) return 1;
            }
        }
    }
    
    return 0;
}

int main() {
    int A, B, C, student;
    
    cin >> A >> B >> C >> student;
    
    cout << solution(A, B, C, student);
    
    return 0;
}
