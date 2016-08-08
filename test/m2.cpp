#include <iostream>

using namespace std;


int solve()
{
	int n, result = 1;

	cin >> n;

	for (int i = 1 ; i <= n ; i++) {
		result = result * i;
		//cout << result << endl;
		for (int j = 1 ; j <= 4 ; j++) {
			if (result % 10 == 0) {
				result = (result / 10);
			}
			else {
				result = result % 1000;
				break;
			}
		}
	}

	return (result % 10);
}

int main(void)
{
	int t;

	cin >> t;
	while(t--) cout << solve() << endl;

	return 0;
}