class Solution {
    fun solution(arr: IntArray) =
        arr.joinToString(""){it.toString()}.count{it=='7'}
}