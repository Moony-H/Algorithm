import kotlin.math.*
class Solution {
    fun solution(arr: IntArray, n: Int) =
        arr.sortedWith{a,b-> val t=abs(a-n)-abs(b-n); if(t==0) a-b else t}[0]
}