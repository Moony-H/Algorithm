class Solution {
    fun solution(s: String, p: String) =
        if(p.uppercase() in s.uppercase()) 1 else 0
}