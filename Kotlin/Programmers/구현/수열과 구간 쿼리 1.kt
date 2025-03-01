class Solution {
    fun solution(l: IntArray, q: Array<IntArray>) =
        l.mapIndexed{ i,n -> n + q.filter{ (s, e) -> i in s..e}.size }
}