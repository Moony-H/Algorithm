class Solution {
    fun solution(s1: String, s2: String) =
        s1.mapIndexed{i,e-> e.toString()+s2[i].toString()}.joinToString("")
}