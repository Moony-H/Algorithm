import kotlin.math.ceil
import kotlin.math.log2
import kotlin.math.pow

class Solution {
    fun solution(arr: IntArray) =
        arr + List((1 shl ceil(log2(arr.size.toDouble())).toInt())-arr.size){0}
}