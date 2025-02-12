class Solution {
    fun solution(rny_string: String) =
        rny_string.map{if(it.toString()=="m") "rn" else it}.joinToString("")
}