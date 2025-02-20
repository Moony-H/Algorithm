class Solution {
    fun solution(n: Int, k: Int) = Array(n){it+1}.filter{it%k==0}
}