#include <iostream>
#include <string>
using namespace std;

string MC[26]={".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
               ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.",
               "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."};

void solve()
{
	int n;
	string mc, t;
	char dc;
	cin >> n;

	for (int i = 0 ; i < n ; i++) {
		cout << "Case " << (i+1) << ": ";
		for (int j = 0 ; j < 5 ; j++) {
			cin >> mc;
			for (int c = 0 ; c < 26 ; c++){
				if (!MC[c].compare(mc)) {
					dc = 'A'+c;
					break;		
				}
			}
			
			if (dc-3 < 'A') dc = 'Z'-3+(dc-'A'+1);
			else dc = dc-3;

			cout << dc;
		}
		cout << endl;
	}
	return;
}

int main(void)
{
	solve();
	return 0;
}