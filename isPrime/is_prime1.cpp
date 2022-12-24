#include <iostream>
#include<math.h>
using namespace std;

bool is_prime(int n)
{
    if (n <= 1)
    {
        return false;
    }

    int length = sqrt(n) + 1;

    for (int i = 2; i < length; i++)
    {
        if (n % i == 0)
        {
            return false;
        }
    }

    return true;
}

int main()
{
    string num = "";

    for (int i = 0; i < 201; i++)
    {
        if (is_prime(i) == true)
        {
            string num = "";
            num = to_string(i);
            cout << num << endl;
        }
    }

    return 0;
}