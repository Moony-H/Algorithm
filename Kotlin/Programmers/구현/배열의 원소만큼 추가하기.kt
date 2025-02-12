class Solution {
    fun solution(arr: IntArray) =
        arr.map{n-> Array(n){n}.toList()}.flatten().toIntArray()
}