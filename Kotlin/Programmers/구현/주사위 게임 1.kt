import kotlin.math.*

class Solution {
    fun solution(a: Int, b: Int) =
        when{
            (a*b)%2!=0 -> a*a+b*b
            (a+b)%2!=0 -> 2*(a+b)
            else -> abs(a-b)
        }
}