class Solution {
    fun solution(b: Int, s: Int): Long {
        if (s == 0 || s == b) return 1
        var result = 1L
        for (i in 0 until s) {
            result = result * (b - i) / (i + 1)
        }
        return result
    }
}