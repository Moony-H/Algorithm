class Solution {
    fun solution(s: String, suffix: String) =
        if(suffix.withIndex().all{(i,e) -> s.getOrNull(s.length-suffix.length+i)==e}) 1 else 0       
}