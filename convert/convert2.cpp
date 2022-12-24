#include <iostream>
using namespace std;

string result(int n, int base)
{
    string result = "";

    while (n > 0)
    {
        result = to_string(n % base) + result;
        n /= base;
    }

    return result;
}


int main()
{
    int n = 18;

    cout << result(n, 2) << endl;
    cout << result(n, 3) << endl;
    cout << result(n, 8) << endl;

    return 0;
}
