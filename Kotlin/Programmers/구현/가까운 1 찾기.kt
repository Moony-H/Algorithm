class Solution {
    fun solution(l: IntArray, idx: Int) =
        (l.mapIndexed{ i,e-> listOf(i,e)}.filterIndexed{ i,e->
            i>=idx && e[1]==1
        }+listOf(listOf(-1,1))).find{it[1]==1}?.get(0)?:-1
}