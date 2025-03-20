class Solution {
    fun solution(arr: IntArray) =
        arr.toList().groupingBy{it}.eachCount().map{listOf(it.key,it.value)}
            .let{c-> c.maxOf{it[1]}.let{m-> c.filter{it[1]==m}}}
            .let{if(it.size==1) it[0][0] else -1}
}