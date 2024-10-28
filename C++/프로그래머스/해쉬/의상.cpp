#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

int solution(vector<vector<string>> clothes)
{
    int answer = 0;
    unordered_map<string, vector<string>> map;
    for (auto &cloth : clothes)
    {
        auto &name = cloth[0];
        auto &type = cloth[1];
        if (map.count(type) == 0)
        {
            map[type] = vector<string>();
        }
        auto &temp = map[type];
        temp.push_back(name);
    }
    int mul = 1;
    for (auto &pair : map)
    {
        auto num = pair.second.size();
        mul *= num + 1;
    }
    return mul - 1;
}