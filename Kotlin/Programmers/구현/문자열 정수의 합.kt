class Solution {
    fun solution(num_str: String) =
        num_str.map{it.toString().toInt()}.sum()
}