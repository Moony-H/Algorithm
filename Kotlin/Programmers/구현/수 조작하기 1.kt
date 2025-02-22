class Solution {
    fun solution(n: Int, c: String) =
        c.map{
            when(it){
                'w'->1
                's'->-1
                'd'->10
                'a'->-10
                else->0
            }
        }.sumOf{it}+n
}