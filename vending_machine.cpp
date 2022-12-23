#include <iostream>
using namespace std;

int main()
{
    int num, input_price, product_price, change;

    num = 8;

    cin >> input_price;
    cin >> product_price;

    change = input_price - product_price;

    int coin[num] = {5000, 1000, 500, 100, 50, 10, 5, 1};

    for (int i = 0; i < num; i++)
    {
        int r = change / coin[i];
        change %= coin[i];
        cout << to_string(coin[i]) + ":" + to_string(r) << endl;
    }

    return 0;
}
