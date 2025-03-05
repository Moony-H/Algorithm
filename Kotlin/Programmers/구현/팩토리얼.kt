class Solution {
    fun solution(n: Int,mul:Int=2):Int =
        if(n<mul) mul-1 else solution(n/mul,mul+1)
}