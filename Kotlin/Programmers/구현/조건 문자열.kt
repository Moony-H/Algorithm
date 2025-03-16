class Solution {
    fun Boolean.toInt()= if(this) 1 else 0
    fun solution(ineq: String, eq: String, n: Int, m: Int) =
        when(ineq+eq){
            ">=" -> n>=m
            "<=" -> n<=m
            ">!" -> n>m
            else -> n<m
        }.toInt()
}