class Solution {
    fun solution(num: Int, k: Int) = num.toString().let{
        if(k.toString() !in it) -1 else it.indexOf(k.toString())+1
    }
}