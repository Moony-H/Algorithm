import kotlin.math.*
class Solution {
    fun solution(dots: Array<IntArray>) =
        abs(dots.maxOf{it[0]}-dots.minOf{it[0]})*abs(dots.maxOf{it[1]}-dots.minOf{it[1]})
}