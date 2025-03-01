class Solution {
    fun solution(s: String, indices: IntArray) =
        s.filterIndexed{i,_-> i !in indices}
}