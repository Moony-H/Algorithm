class Solution {
    fun solution(n: Int,now:Int=1):Int{
        if(n==0) return now -1
        return if(now%3==0 || "3" in now.toString()) solution(n,now+1) else solution(n-1,now+1)
    }
}