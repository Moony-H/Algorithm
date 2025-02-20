class Solution {
    fun solution(q: Int, r: Int, code: String) =
        code.filterIndexed{i,_-> i%q==r}
}