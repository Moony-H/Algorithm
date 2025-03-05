class Solution {
    fun solution(e: IntArray) =
        e.withIndex().sortedBy{-it.value}.withIndex().sortedBy{it.value.index}
            .map{it.index+1}
}