class Solution {
    fun solution(s: Array<IntArray>) =
        s.map{it.sum()/it.size.toFloat()}.withIndex().sortedByDescending{it.value}.withIndex()
        .foldIndexed(listOf<List<Float>>()){i,acc,e-> 
            if(i==0)
                listOf(listOf(e.value.index.toFloat(),(i+1).toFloat(),e.value.value))
            else{
                if(acc.last()[2]==e.value.value)
                    acc+listOf(listOf(e.value.index.toFloat(),acc.last()[1],e.value.value))
                else
                    acc+listOf(listOf(e.value.index.toFloat(),(i+1).toFloat(),e.value.value))
            }
        }.sortedBy{it[0]}.map{it[1].toInt()}
}