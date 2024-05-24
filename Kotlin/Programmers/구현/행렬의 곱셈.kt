class Solution {
    fun solution(arr1: Array<IntArray>, arr2: Array<IntArray>): Array<IntArray> {
        var answer = arrayListOf<ArrayList<Int>>()
        arr1.forEach{
            val tempList=arrayListOf<Int>()
            for(i in 0 until arr2[0].size){
                var result=0
                for(j in 0 until arr2.size){
                    result+=(it[j]*arr2[j][i])
                }
                tempList.add(result)
            }
            answer.add(tempList)
        }
        return Array<IntArray>(answer.size){
            answer[it].toIntArray()
        }
    }
}