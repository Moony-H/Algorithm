class Solution {
    fun solution(l: IntArray, n: Int) =
        List(l.size/n){i-> List(n){j-> l[i*n+j]}}
}