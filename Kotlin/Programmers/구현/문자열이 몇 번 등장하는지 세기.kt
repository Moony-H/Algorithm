class Solution {
    fun solution(s: String, pat: String) =
        s.mapIndexed{
            i,_-> if(i+pat.length<=s.length && s.substring(i,i+pat.length)==pat) 1 else 0
        }.sum()
}