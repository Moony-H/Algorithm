class Solution {
    fun solution(i: Int, j: Int, k: Int) =
        List(j-i+1){it+i}.joinToString("").count{it.toString().toInt()==k}
}