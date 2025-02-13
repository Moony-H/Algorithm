class Solution {
    fun solution(s: String, a: String) =
        s.map{if(it.toString()==a) it.uppercase() else it}.joinToString("")
}