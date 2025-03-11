class Solution {
    fun solution(arr: IntArray) =
        arr.withIndex().filter{it.value==2}.let{
            if(it.isEmpty()) listOf(-1)
            else{
                val s=it[0]
                val e=it.getOrNull(1)?: return listOf(2)
                println("${s.index} ${e.index}")
                arr.slice(s.index..e.index)
            }
        }
}