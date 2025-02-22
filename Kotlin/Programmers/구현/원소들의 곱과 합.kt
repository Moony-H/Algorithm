import kotlin.math.pow

class Solution {
    fun solution(l: IntArray) =
        if(l.reduce{acc,i-> acc*i}<(l.sumOf{it}).toDouble().pow(2)) 1 else 0
}