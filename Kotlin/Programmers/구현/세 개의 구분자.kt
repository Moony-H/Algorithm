class Solution {
    fun solution(s: String) =
        s.split("a","b","c").filter{it.isNotBlank()}
}