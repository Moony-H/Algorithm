class Solution {
    fun solution(n: IntArray, d: String) =
        n.mapIndexed{i,_-> if(d=="right") n[(i-1+n.size)%n.size] else n[(i+1)%n.size]}
}