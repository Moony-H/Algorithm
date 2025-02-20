class Solution {
    fun solution(s: String, p: String) =
        if(p.withIndex().all{(i,e)-> s.getOrNull(i)==e}) 1 else 0
}