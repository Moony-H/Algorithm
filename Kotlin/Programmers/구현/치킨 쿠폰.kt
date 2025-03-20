class Solution {
    fun solution(c: Int):Int{
        var r=c
        var answer=0
        while(r>=10){
            answer+=r/10
            r=r/10+r%10
        }
        return answer
    }
}