class Solution {
    fun solution(arr: IntArray, q: Array<IntArray>) =
        arr.mapIndexed{i,n->
            n+q.sumOf{(s,e,k)-> if(i in s..e && i % k == 0) 1.toInt() else 0}
        }
}