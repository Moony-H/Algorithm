import java.util.*

class Solution {
    fun solution(l: IntArray, q: Array<IntArray>) =
        q.fold(l.toList()){acc, e-> Collections.swap(acc,e[0],e[1]); acc}
}