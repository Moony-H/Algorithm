#include <iostream>
#include <string>

using namespace std;

int main()
{
    long n = 0;
    int b = 0;
    cout << "fuck" << endl;
    string answer = "";
    cin >> n >> b;
    while (n != 0)
    {
        int temp = n % b;
        answer += temp > 9 ? char(temp - 10 + 65) : char(temp) + '0';

        n = n / b;
    }
    cout << answer << endl;
}