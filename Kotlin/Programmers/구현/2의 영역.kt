class Solution {
    fun solution(arr: IntArray):List<Int>{
        val temp=arr.withIndex().filter{it.value==2}
        if(temp.isEmpty()) return listOf(-1)
        if(temp.size==1) return listOf(2)
        return arr.slice(temp[0].index..temp.last().index).toList()
    }
}