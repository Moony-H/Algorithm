#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    unordered_map<string,int> map;
    for(auto &p:participant)
    {
        map[p]=map[p]+1;
    }
    for(auto &c:completion)
    {
        map[c]-=1;
    }
    for(auto &pair:map){
        if(pair.second!=0)
        {
            return pair.first;
        }
    }
    return answer;
}