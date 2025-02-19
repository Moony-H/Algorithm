class Solution {
    fun solution(l: IntArray, n: Int) =
        l.toList().subList(n,l.size)+l.toList().subList(0,n)
}