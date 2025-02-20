class Solution {
    fun solution(lines: Array<IntArray>) =
        lines.sortedBy{it[0]}.let{ l ->
            val changed = l.map{(s,e)-> listOf(s-l[0][0],e-l[0][0])}
            val table = Array(changed.maxOf{e-> e[1]}+1){0}
            changed.forEach{(s,e)-> for(i in s until e){table[i]+=1}}
            table.filter{it>1}.size
        }
}