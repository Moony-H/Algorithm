class Solution {
    fun solution(s: String) =
        s.map{if(it.toInt()<'l'.toInt()) 'l' else it}.joinToString("")
}