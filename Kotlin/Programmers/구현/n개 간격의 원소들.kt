class Solution {
    fun solution(l: IntArray, n: Int) =
        l.filterIndexed{i,e-> i%n==0}
}