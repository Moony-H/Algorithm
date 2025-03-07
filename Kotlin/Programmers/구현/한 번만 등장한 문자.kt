class Solution {
    fun solution(s: String) =
        s.filter{c-> s.count{it==c}==1}.toList().sorted().joinToString("")
}