#include <iostream>
#include <queue>

using namespace std;

// Open
int reachToW(char map[50][50], int i, int j, int M, int N)
{
	char map2[50][50];
	int ret = 0;

	//cout << "rTW" << endl;
	
	if (i <= 0 || i >= N-1) return 1;
	
	if (j <= 0 || j >= M-1) return 1;

	if (map[i][j] == '1' || map[i][j] == 'C' || map[i][j] == 'T') return 0; 

	memcpy(map2, map, 50*50*sizeof(char));

	map2[i][j] = 'T';

	// UP
	if (map2[i-1][j] == '0') {
		if (reachToW(map2, i-1, j, M, N))
			return 1;
	}

	// DOWN
	if (map2[i+1][j] == '0') {
		if (reachToW(map2, i+1, j, M, N))
			return 1; 
	}

	// LEFT
	if (map2[i][j-1] == '0') {
		if (reachToW(map2, i, j-1, M, N))
			return 1; 
	}

	// RIGHT
	if (map2[i][j+1] == '0') {
		if (reachToW(map2, i, j+1, M, N))
			return 1;
	}

	return ret;
}

int melt(char map[50][50], int nSnow, int M, int N)
{
	int count = 0;

	while (nSnow > 0) {
		cout << "nSnow : " << nSnow << endl;

		for (int i = 0 ; i < N ; i++) {
			for (int j = 0 ; j < M ; j++) {
								
				if (map[i][j] == '1') {
					
					//cout << i << " " << j << endl;

					int flag = 0;

					if ((i == 0) || (map[i-1][j] == '0')) {
						if (reachToW(map, i-1, j, N, M))
							flag++;
					}

					if ((i == N-1) || (map[i+1][j] == '0')) {
						if (reachToW(map, i+1, j, N, M))
							flag++;
					}

					if ((j == 0) || (map[i][j-1] == '0')) {
						if (reachToW(map, i, j-1, N, M))
							flag++;
					}

					if ((j == M-1) || (map[i][j+1] == '0')) {
						if (reachToW(map, i, j+1, N, M))
							flag++;
					}

					if (flag >= 2) {
						map[i][j] = 'C';
						nSnow--;
					}
				}
			}
		}

		// Clear
		for (int i = 0 ; i < N ; i++)
			for (int j = 0 ; j < M ; j++)
				if (map[i][j] == 'C')
					map[i][j] = '0';
		count++;
	}

	return count;
}

int car(char map[50][50], int M, int N)
{

	return 0;
}

void solve()
{
	int M, N;
	char map[50][50];
	int nSnow = 0;

	cin >> M >> N;

	for (int i = 0 ; i < N ; i++) {
		for (int j = 0 ; j < M ; j++) {
			cin >> map[i][j];
			if (map[i][j] == '1')
				nSnow++;
		}
	}

	cout << melt(map, nSnow, M, N) << " " << car(map, M, N) << endl;

	return;
}

int main(void)
{
	int t;
	cin >> t;
	
	while(t--) solve();

	return 0;
}