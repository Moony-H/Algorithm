class Solution {
    fun solution(str: String, q: Array<IntArray>) =
        q.fold(str){s,e-> s.slice(0 until e[0])+s.slice(e[0]..e[1]).reversed()+s.slice(e[1]+1 until s.length)}
}