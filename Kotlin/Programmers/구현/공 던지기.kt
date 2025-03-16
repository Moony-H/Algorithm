class Solution {
    fun solution(n: IntArray, k: Int) =
        n[((k-1)*2)%n.size]
}