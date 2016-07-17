#include <iostream>
#include <cstdio>
#include <utility>
#include <queue>
#include <stack>

const int INF = 10000000;
const int MAX_N = 20;
const int MAX_M = 20;

char maze[MAX_N][MAX_M+1];
int d[MAX_N][MAX_M];


void solve()
{
	// Loop to search S
	// Start from S

	// Pop 
	// Find next moves around S	
	// Push next moves to the queue
	// Update d[next_x][next_y] = d[x]d[y] + 1
	// If G is found, then return d[G_x]d[G_y]
}

int main()
{
	int N,M;

	cin >> N, M;

	for (int i = 0 ; i < N ; i++)
		for (int j = 0 ; j < M ; j++) {
			cin >> maze[i][j];
			d[i][j] = INF;
		}

	return 0;
}