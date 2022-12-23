#include <iostream>
using namespace std;

int main()
{
    int length = 10;
    int data[] = {6, 15, 4, 2, 8, 5, 11, 9, 7, 13};

    for (int i = 0; i < length; i++)
    {
        int min = i;

        for (int j = i + 1; j < length; j++)
        {
            if (data[min] > data[j])
            {
                min = j;
            }
        }

        int min_data = data[min];
        data[min] = data[i];
        data[i] = min_data;
    }

    for (int i = 0; i < length; i++)
    {
        cout << data[i] << endl;
    }

    return 0;
}
