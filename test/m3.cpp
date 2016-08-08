#include <iostream>

using namespace std;

const int DIV = 20150523;

int solve()
{
	int a, b, count = 0, tmp = 0;

	cin >> a >> b;

	for (int i = a ; i <= b ; i++) {
		//cout << "# " << i << '\n';
		if (i % 3 == 0) {
			count = (count + 1) % DIV;
			//cout << count << '\n';
		}
		else {
			tmp = i;
			while (tmp != 0) {
				int t = tmp % 10;
				if ((t == 3) ||
					(t == 6) ||
					(t == 9)) {
					count = (count + 1) % DIV;
					//cout << count << '\n';
					break;
				}
				tmp = tmp / 10;
			}
		}
	}

	return count;
}

int main(void)
{
	cout << solve() << endl;

	return 0;
}