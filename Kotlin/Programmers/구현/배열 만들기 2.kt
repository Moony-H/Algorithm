class Solution {
    fun solution(l: Int, r: Int) =
        (l..r).filter{it.toString().all{it=='0' || it=='5'}}.let{if(it.isEmpty()) listOf(-1) else it}
}