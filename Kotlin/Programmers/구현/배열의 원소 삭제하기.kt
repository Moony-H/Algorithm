class Solution {
    fun solution(arr: IntArray, l: IntArray) =
        arr.filter{it !in l}
}