class Solution {
    fun solution(s: String, pat: String) =
        s.substring(0,s.lastIndexOf(pat)+pat.length)
}