class Solution {
    fun solution(b: Array<IntArray>, k: Int) =
        List(b.size){i->List(b[i].size){j-> listOf(i,j)}}
            .flatten().filter{it.sum()<=k}.sumOf{(i,j)->b[i][j]}
}