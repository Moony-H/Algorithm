class Solution {
    fun solution(l: Array<String>, f: BooleanArray) =
        l.filterIndexed{i,_ -> !f[i]}
}