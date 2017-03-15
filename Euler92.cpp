#include <iostream>

using namespace std;

// converts n to a string then accesses each individual char, squares it, and adds to a sum
int sqr_digit_sum(int n) {
	int sum = 0;
	string s = to_string(n);
	for (int i = 0; i < s.length(); i++) {
		int digit = s[i] - '0';
		sum += digit * digit;
	}
	return sum;
}

int main() {

	int count = 0;
	int max = 10000000;

	for (int i = 1; i < max; i++) {

		int sds = sqr_digit_sum(i);

		while (sds != 1 && sds != 89) {
			sds = sqr_digit_sum(sds);
		}

		if (sds != 1) {
			count++;
		}

	}
	cout << count << endl;

	return 0;
}