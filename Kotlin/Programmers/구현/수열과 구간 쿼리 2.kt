class Solution {
    fun solution(arr: IntArray, q: Array<IntArray>) =
        q.map{(s,e,k)-> arr.sliceArray(s..e).filter{it>k}.minOrNull()?:-1}
}