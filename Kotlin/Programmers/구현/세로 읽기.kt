class Solution {
    fun solution(s: String, m: Int, c: Int) =
        s.filterIndexed{i,_-> i%m==(c-1)}
}