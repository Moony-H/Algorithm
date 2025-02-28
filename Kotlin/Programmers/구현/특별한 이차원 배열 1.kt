class Solution {
    fun solution(n: Int) =
        List(n){i-> List(n){j -> if(i==j) 1 else 0}}
}