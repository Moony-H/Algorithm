class Solution {
    fun solution(o: Int) = o.toString().map{it.toInt()-48}.filter{it%3==0 && it!=0}.size
}