class Solution {
    fun solution(age: Int) =
        age.toString().map{(it.toString().toInt()+97).toChar()}.joinToString("")
}