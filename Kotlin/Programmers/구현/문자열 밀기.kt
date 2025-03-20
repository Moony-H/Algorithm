class Solution {
    fun solution(a: String, b: String)=
        a.mapIndexed{i,_-> a.takeLast(i%a.length)+a.dropLast(i%a.length)}.indexOf(b)
}