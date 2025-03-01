class Solution {
    fun solution(s: String) = s.split("x").filter{it.isNotBlank()}.sorted()
}