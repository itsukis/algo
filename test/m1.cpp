#include <iostream>
#include <vector>

using namespace std;

const int MAX = 200;

void solve()
{
	int z, n;
 	string in;
 	int val = 0, pos = 0 , len = 0;
 	string sub;

	cin >> z >> n;
	cin >> in;

	while(pos < in.size()) {
		for (len = 1 ; len < (in.size()-pos) ; len++) {
			sub = in.substr(pos, len);
			cout << sub << ' ' << pos << ' ' << len << ' ' << in.find(sub, pos+len) << '\n';
			if (in.find(sub, pos+len) == -1) {
				cout << val++ << "->" << sub << '\n';
				break;
			}
		}
		if (pos + len >= in.size())
			cout << val++ << "->" << in.substr(pos, in.size()-pos) << '\n';
		
		pos = pos + len;
	}

	return;
}

int main(void)
{
	int t;

	cin >> t;
	while(t--) solve();

	return 0;
}