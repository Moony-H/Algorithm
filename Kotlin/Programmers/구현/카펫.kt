class Solution {
    fun solution(brown: Int, yellow: Int): IntArray {
        for(i in 1..yellow){
            if(yellow%i!=0)
                continue
            val yW=yellow/i
            if((i*2+4+(yW)*2)==brown)
                return intArrayOf(yellow/i+2,i+2)
        }
        return intArrayOf()
    }
}