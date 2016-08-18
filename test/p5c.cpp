#include <iostream>
#include <queue>

using namespace std;

// Open
int reachToW(char map[50][50], int i, int j, int M, int N)
{
	int ret = 0;

	if (i <= 0 || i >= N-1) return 1;
	
	if (j <= 0 || j >= M-1) return 1;

	if (map[i][j] == 'W') return 1;

	if (map[i][j] == '1' || map[i][j] == 'C' || map[i][j] == 'T') return 0; 

	map[i][j] = 'T';

	if (map[i-1][j] == 'W' || 
		map[i][j-1] == 'W' ||
		map[i+1][j] == 'W' ||
		map[i][j+1] == 'W') {
		map[i][j] = 'W';
		return 1;
	}

	// UP
	if (map[i-1][j] == '0') {
		if (reachToW(map, i-1, j, M, N)) {
			map[i][j] = 'W';
			return 1;
		}
	}

	// LEFT
	if (map[i][j-1] == '0') {
		if (reachToW(map, i, j-1, M, N)) {
			map[i][j] = 'W';
			return 1; 
		}
	}

	// DOWN
	if (map[i+1][j] == '0') {
		if (reachToW(map, i+1, j, M, N)) {
			map[i][j] = 'W';
			return 1; 
		}
	}

	// RIGHT
	if (map[i][j+1] == '0') {
		if (reachToW(map, i, j+1, M, N)) {
			map[i][j] = 'W';
			return 1;
		}
	}

	return ret;
}

int melt(char imap[50][50], int nSnow, int M, int N)
{
	char map[50][50];
	int count = 0;

	memcpy(map, imap, 50*50*sizeof(char));

	while (nSnow > 0) {
		for (int i = 0 ; i < N ; i++) {
			for (int j = 0 ; j < M ; j++) {
								
				if (map[i][j] == '1') {
					
					//cout << i << " " << j << endl;

					int flag = 0;

					// UP
					if (map[i-1][j] != '1') {
						if (reachToW(map, i-1, j, N, M))
							flag++;
					}

					// LEFT
					if (map[i][j-1] != '1') {
						if (reachToW(map, i, j-1, N, M))
							flag++;
					}

					// DOWN
					if (map[i+1][j] != '1') {
						if (reachToW(map, i+1, j, N, M))
							flag++;
					}

					// RIGHT
					if (map[i][j+1] != '1') {
						if (reachToW(map, i, j+1, N, M))
							flag++;
					}

					if (flag >= 2) {
						map[i][j] = 'C';
						nSnow--;
					}

					for (int i = 0 ; i < N ; i++)
						for (int j = 0 ; j < M ; j++)
							if (map[i][j] == 'T')
								map[i][j] = '0';	

				}
			}
		}

		/*
		// Print
		for (int i = 0 ; i < N ; i++) {
			for (int j = 0 ; j < M ; j++) {
				cout << map[i][j] << ' ';
			}
			cout << '\n';
		}
		cout << "-----" << endl;
		//
		*/

		// Clear
		for (int i = 0 ; i < N ; i++)
			for (int j = 0 ; j < M ; j++)
				if (map[i][j] == 'C')
					map[i][j] = '0';
		count++;
	}

	return count;
}

void dfs(char map[50][50], int i, int j, int M, int N)
{
	int count = 0;

	if ((map[i-1][j] != '1') &&
		(map[i+1][j] != '1') &&
		(map[i][j-1] != '1') &&
		(map[i][j+1] != '1')) {
		
		map[i][j] = '0';
		return;
	}

	map[i][j] = 'C';

	// UP
	if (map[i-1][j] == '1')
		dfs(map, i-1, j, M, N);

	// DOWN
	if (map[i+1][j] == '1')
		dfs(map, i+1, j, M, N);

	// LEFT
	if (map[i][j-1] == '1')
		dfs(map, i, j-1, M, N);

	// RIGHT
	if (map[i][j+1] == '1')
		dfs(map, i, j+1, M, N);

	map[i][j] = '0';

	return;
}

int car(char imap[50][50], int M, int N)
{
	char map[50][50];
	int count = 0;

	memcpy(map, imap, 50*50*sizeof(char));

	for (int i = 0 ; i < N ; i++) {
		for (int j = 0 ; j < M ; j++) {
			if (map[i][j] == '1') {

				map[i][j] = 'C';

				if (map[i-1][j] == '1')
					dfs(map, i-1, j, M, N);

				if (map[i+1][j] == '1')
					dfs(map, i+1, j, M, N);

				if (map[i][j-1] == '1')
					dfs(map, i, j-1, M, N);

				if (map[i][j+1] == '1')
					dfs(map, i, j+1, M, N);

				map[i][j] = '0';

				count++;
			}
		}
	}

	return count;
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