class Solution {
    fun solution(l: Array<String>, ex: String) =
        l.filter{ex !in it}.joinToString("")
}