class Solution {
    fun solution(l: IntArray) =
        if(l.size>= 11) l.sum() else l.reduce{acc, n-> acc*n}
}