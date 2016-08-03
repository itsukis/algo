#include <iostream>
#include <string>
using namespace std;

void solve()
{
	string s;

	cin >> s;

	int i = s.size()-1, j = 0, f = 0, c = 0; 
	for (j = 0 ; j < s.size() ; j++) {
		cout << s[j] << " " << s[i] << endl;
		if (i <= j) break;
		
		if (s[i] != s[j]) {
			c++;
			if (f != 0) {
				f = 0;
				break;
			}
		} else {
			i--;
			f = 1;
		}
	}

	if (f == 1 && c == 0)
		cout << s.size() << endl;
	else if (f == 1 && c != 0)
		cout << s.size() + c << endl;
	else
		cout << 2*s.size()-1 << endl;

	return;
}

int main()
{
	int t;

	cin >> t;
	
	while(t--) solve();

	return 0;
}

/*

abcaaba

abcaababaacba

*/