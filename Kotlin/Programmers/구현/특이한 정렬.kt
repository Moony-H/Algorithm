import kotlin.math.*
class Solution {
    fun solution(l: IntArray, n: Int) = 
        l.sortedDescending().sortedWith{a,b-> abs(n-a) - abs(n-b)}
}