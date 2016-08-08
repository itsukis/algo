#include <iostream>

using namespace std;

void solve()
{
	int a, b, S;
	int d1, d2, tS;

	cin >> a >> b >> S;

	d1 = S/a; d2 = S/b;

	if (d1 == 0 && d2 == 0) {
		cout << "Impossible" << endl;
		return;
	}

	if (a >= b) {
		for (int i = d1 ; i >= 0 ; i--) {
			tS = S - i*a;
			if (tS % b == 0) {
				cout << i << ' ' << tS/b << endl;
				return;
			}
		}

	}
	else {
		for (int i = d2 ; i >= 0 ; i--) {
			tS = S - i*b;
			if (tS % a == 0) {
				cout << tS/a << ' ' i << endl;
				return;
			}
		}
	}

	cout << "Impossible" << endl;

	return;
}

int main(void)
{
	int t;
	cin >> t;
	
	while(t--) solve();

	return 0;
}