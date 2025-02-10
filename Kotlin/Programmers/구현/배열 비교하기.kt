class Solution {
    fun solution(arr1: IntArray, arr2: IntArray):Int{
        if(arr1.size>arr2.size)
            return 1
        if(arr1.size<arr2.size)
            return -1
        val ar1=arr1.sum()
        val ar2=arr2.sum()
        if(ar1>ar2)
            return 1
        if(ar2>ar1)
            return -1
        return 0
    }

}