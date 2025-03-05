class Solution {
    fun solution(s: String) =
        s.split("[^0-9]".toRegex()).filter{it.isNotBlank()}.sumOf{it.toInt()}
}