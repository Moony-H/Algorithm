class Solution {
    fun solution(n: Int, t: Int)=
        (-1000..1000).find{e->(e..e+n-1).sum()==t}!!.let{num-> List(n){num+it}}
}