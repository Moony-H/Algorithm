class Solution {
    fun solution(a: Int, d: Int, included: BooleanArray) =
        included.foldIndexed(0){i,acc,e-> acc+if(included[i]) a+i*d else 0}
}