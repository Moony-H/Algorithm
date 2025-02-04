import java.util.*


class Solution {
    

    fun solution(jobs: Array<IntArray>): Int {
        val result=arrayListOf<Int>()
        val jobQ=jobs.mapIndexed{i,e-> Triple(i,e[0],e[1])}.sortedBy{it.second}.toCollection(arrayListOf())
        val pq=PriorityQueue<Triple<Int,Int,Int>>({a,b->
            val timeDiff=a.third-b.third
            val requestTimeDiff=a.second-b.second
            if(timeDiff==0 && requestTimeDiff==0){
                a.first-b.first
            }else if(timeDiff==0){
                requestTimeDiff
            }else{
                timeDiff
            }
        }) //번호, 요청 시각, 소요시간
        var startTime=0
        var nowTime=0
        var runningRequest:Triple<Int,Int,Int>? =null
        while(runningRequest!=null || pq.isNotEmpty() || jobQ.isNotEmpty()){
            while(jobQ.getOrNull(0)?.second==nowTime){
                pq.add(jobQ[0])
                jobQ.removeFirst()
            }
            if(runningRequest!=null && runningRequest.third==(nowTime-startTime)){
                result.add(nowTime-runningRequest.second)
                runningRequest=null
            }
            
            if(runningRequest==null && pq.isNotEmpty()){
                runningRequest=pq.poll()
                startTime=nowTime
            }
            nowTime+=1
            
        }
        return result.sum()/result.size
    }
}