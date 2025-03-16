class Solution {
    fun solution(s: IntArray) =
        s.minOf{it} + (s.sumOf{it}-s.maxOf{it}-1)
}