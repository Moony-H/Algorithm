#include <vector>
#include <unordered_map>
#include <iostream>
using namespace std;

int solution(vector<int> nums)
{
    unordered_map<int,int> map;
    int answer = 0;
    
    for(int i=0; i<nums.size();i++)
    {
        auto temp=nums[i];
        map[temp]=map[temp]+1;
    }
    
    int a=nums.size()/2;
    for (const auto& pair : map) {
        answer+=1;
    }
    
    return answer>a?a:answer;
}