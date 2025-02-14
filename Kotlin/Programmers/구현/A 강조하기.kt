class Solution {
    fun solution(s: String) =
        s.map{it.toString()}.map{if(it=="a") "A" else if (it!="A") it.lowercase() else it}.joinToString("")
}