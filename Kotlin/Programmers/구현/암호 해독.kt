class Solution {
    fun solution(s: String, c: Int) =
        s.filterIndexed{i,_-> (i+1)%c==0}
}