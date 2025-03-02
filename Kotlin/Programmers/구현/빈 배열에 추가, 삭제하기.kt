class Solution {
    fun solution(arr: IntArray, flag: BooleanArray) =
        flag.foldIndexed(listOf<Int>()){i,acc,e->
            if(e) acc+List(arr[i]*2){arr[i]}
            else acc.dropLast(arr[i])
        }
}