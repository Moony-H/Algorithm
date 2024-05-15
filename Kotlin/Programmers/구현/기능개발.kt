class Solution {
    fun solution(progresses: IntArray, speeds: IntArray): IntArray {
        var answer=ArrayList<Int>()
        var result = ArrayList<Int>()
        var day=0
        progresses.forEachIndexed{i,item->
            val s=speeds[i]
            val remain=100-item
            val pDay=remain/s+if(remain%s==0)0 else 1
            if(day<pDay){
                day=pDay
            }
            result.add(day)
        }
        val hash=HashMap<Int,Int>()
        result.forEach{
            hash[it]=(hash[it]?:0)+1
        }
        result.distinct().forEach{
            hash[it]?.let{
                answer.add(it)
            }
        }
        return answer.toIntArray()
        
    }
}