class Solution {
    fun solution(arr: Array<IntArray>) =
        arr.map{it.toList() + if(arr.size>it.size) List(arr.size-it.size){0} else listOf<Int>()} + 
        if(arr.size<arr[0].size) List(arr[0].size-arr.size){List(arr[0].size){0}} else listOf<List<Int>>()
}