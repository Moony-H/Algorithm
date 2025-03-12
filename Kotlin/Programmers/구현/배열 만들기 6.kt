class Solution {
    fun solution(arr: IntArray):List<Int>{
        val answer=arr.foldIndexed(listOf<Int>()){i,acc,e->
            when{
                acc.isEmpty()-> listOf(e)
                acc.last()==e -> acc.dropLast(1)
                else-> acc+listOf(e)
            }
        }
        return if(answer.isEmpty()) listOf(-1) else answer
    }
}