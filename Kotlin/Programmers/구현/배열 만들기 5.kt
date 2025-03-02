class Solution {
    fun solution(strs: Array<String>, k: Int, s: Int, l: Int) =
        strs.map{it.substring(s,s+l).toInt()}.filter{it>k}
}