#include <iostream>
#include <vector>

using namespace std;

int solve()
{
	int result = 0;
	vector <int> v;

	v.push_back(1);
	v.push_back(2);
	v.push_back(3);

	for (int i = 0 ; i < v.size() ; i++)
		cout << v[i];
	cout << '\n';

	v.erase(v.begin());

	for (int i = 0 ; i < v.size() ; i++)
		cout << v[i];	

	return result;
}

int main()
{
	int t;

	cin >> t;

	while(t--) cout << solve() << '\n';

	return 0;
}