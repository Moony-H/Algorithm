import kotlin.math.log2

class Solution {
    fun solution(l: IntArray) = l.map{log2(it.toDouble()).toInt()}.sum()
}