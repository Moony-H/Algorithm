class Solution {
    fun solution(p: Array<String>, k: Int) =
        p.flatMap { r -> List(k) { r.flatMap {c-> List(k){c} }.joinToString("") }}
}