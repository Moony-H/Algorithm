import kotlin.math.*
class Solution {
    fun solution(r: IntArray, a: BooleanArray) =
        r.withIndex().filterIndexed{i,e-> a[i]}.sortedBy{it.value}
            .slice(0..2).foldIndexed(0){i,acc,e-> acc+10.0.pow(4-(i*2)).toInt()*e.index}
}