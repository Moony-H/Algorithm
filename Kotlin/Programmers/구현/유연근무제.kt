class Solution {
    fun Int.toTime() = this.toString().let{it.takeLast(2).toInt()+it.dropLast(2).toInt()*60}
    fun solution(s: IntArray, tLog: Array<IntArray>, sDay: Int)=
        tLog.map{t->t.filterIndexed{i,e-> (i+sDay-1)%7+1 in 1..5}.map{it.toTime()}}.let{t->
            s.filterIndexed{i,e-> t[i].all{it<=e.toTime()+10}}.count()
        }
}