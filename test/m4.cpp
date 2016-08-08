#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int lotto(vector<int> nums, int s, int n, int m) 
{
	int count = 0, d = n-s-1;

	if (s == n) {
		//* Debug
		for (int i = 0 ; i < n ; i++)
			cout << nums[i] << " ";
		cout << endl;
		//*/ 
		return 1;
	}

	while(nums[s] * pow(2, d) <= m) {
		nums[s+1] = nums[s] * 2;
		count = count + lotto(nums, s+1, n, m);
		nums[s] = nums[s] + 1;
	}

	return count;
}

int solve()
{
	int n, m, count = 0;
	//vector<int> base = {1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024};
	vector<int> base = {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

	cin >> n >> m;

	count = lotto(base, 0, n, m);

	return count;
}

int main(void)
{
	int t;
	cin >> t;
	
	while(t--) cout << solve() << endl;

	return 0;
}