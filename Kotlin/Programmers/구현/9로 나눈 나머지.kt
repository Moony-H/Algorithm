class Solution {
    fun solution(n: String) = 
        n.sumOf{it.toString().toInt()}%9
}