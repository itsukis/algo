#include <iostream>
using namespace std;

void test(char m[3][3]) {
	m[0][0] = '9';

}

int main()
{
	char m[3][3] = {{'0', '0' ,'0'},{'0', '0' ,'0'}, {'0', '0', '0'}};

	test(m);

	for (int i = 0 ; i < 3 ; i++)
		for (int j = 0; j < 3 ; j++)
			cout << m[i][j] << endl;

	return 0;
}