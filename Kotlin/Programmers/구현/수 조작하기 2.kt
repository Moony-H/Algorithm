class Solution {
    fun solution(n: IntArray) =
        n.mapIndexed{i,e->
            when{
                i==0-> ""
                e-n[i-1]==1->"w"
                e-n[i-1]==-1->"s"
                e-n[i-1]==10->"d"
                e-n[i-1]==-10->"a"
                else->""
            }
        }.joinToString("")
}