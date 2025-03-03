class Solution {
    fun solution(str: String, s: Int, e: Int) =
        str.substring(0,s)+str.substring(s,e+1).reversed()+str.substring(e+1)
}