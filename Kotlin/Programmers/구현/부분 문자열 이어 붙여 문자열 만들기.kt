class Solution {
    fun solution(s: Array<String>, p: Array<IntArray>) =
        s.mapIndexed{i,e-> e.substring(p[i][0]..p[i][1])}.joinToString("")
}