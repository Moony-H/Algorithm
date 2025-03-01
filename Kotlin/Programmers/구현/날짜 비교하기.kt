class Solution {
    fun solution(d1: IntArray, d2: IntArray) =when{
        d1[0]<d2[0]-> 1
        d1[0]==d2[0] &&d1[1]<d2[1]-> 1
        d1[0]==d2[0] &&d1[1]==d2[1] &&d1[2]<d2[2]-> 1
        else -> 0
    }
}