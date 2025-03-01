class Solution {
    fun solution(arr: IntArray, intervals: Array<IntArray>) =
        intervals.map{arr.slice(it[0]..it[1])}.flatten()
}