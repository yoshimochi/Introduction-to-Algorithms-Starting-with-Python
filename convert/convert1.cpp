#include <iostream>
using namespace std;

int main()
{
    int n = 18;
    string result = "";

    while (n > 0)
    {
        result = to_string(n % 2) + result;
        n /= 2;
    }
    cout << result << endl;

    return 0;
}
