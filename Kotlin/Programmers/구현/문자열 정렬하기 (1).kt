class Solution {
    fun solution(s: String) =
        s.filter{it.toString().matches("[0-9]".toRegex())}.map{it.toString().toInt()}.sorted()
}