#include <iostream>

using namespace std;

#define MAX (a >= b ? a : b)
#define MIN (a < b  ? a : b)

void solve()
{
	int a, b, S;
	int tS;

	cin >> a >> b >> S;

	if (S/a == 0 && S/b == 0) {
		cout << "Impossible" << endl;
		return;
	}


	for (int i = (S/MAX) ; i >= 0 ; i--) {
		tS = S - (i*MAX);
		if (tS % MIN == 0) {
			if (a >= b)
				cout << i << ' ' << (tS/MIN) << endl;
			else
				cout << (tS/MIN) << ' ' << i << endl;
			return;
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