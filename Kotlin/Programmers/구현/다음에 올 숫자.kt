class Solution {
    fun solution(common: IntArray):Int{
        val pDiff=common[1]-common[0]
        if(pDiff==common[2]-common[1]) return common.last()+pDiff
        val ratio=common[1]/common[0]
        return common.last()*ratio
    }
}