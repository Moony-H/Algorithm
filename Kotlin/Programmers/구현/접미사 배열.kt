class Solution {
    fun solution(s: String) =
        s.mapIndexed{i,_-> s.substring((s.length-i-1) until s.length)}.sorted()
}