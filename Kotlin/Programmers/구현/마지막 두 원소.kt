class Solution {
    fun solution(l: IntArray) =
        l.toList()+if(l.last()>l[l.size-2]) listOf(l.last()-l[l.size-2]) else
    listOf(l.last()*2)
}