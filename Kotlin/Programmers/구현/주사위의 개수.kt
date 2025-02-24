class Solution {
    fun solution(box: IntArray, n: Int) =
        box.fold(1){acc,e-> acc*(e/n)}
}