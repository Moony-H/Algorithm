import java.util.*

class Solution {
    fun solution(operations: Array<String>): IntArray {
        var answer = intArrayOf()
        val hash=hashMapOf<Int,Int>()
        val minPq=PriorityQueue<Int>()
        val maxPq=PriorityQueue<Int>(reverseOrder())
        operations.forEach{operation->
            val oper=operation.split(" ")
            val command=oper[0]
            val num=oper[1].toInt()
            if (command=="D"){
                if(num==-1){
                    while(minPq.isNotEmpty() && hash[minPq.peek()]==0){
                        minPq.poll()
                    }
                    if(minPq.isNotEmpty()){
                        val temp=minPq.poll()
                        hash[temp]=(hash[temp]?:0)-1
                    }
                }else{
                    while(maxPq.isNotEmpty() && hash[maxPq.peek()]==0){
                        maxPq.poll()
                    }
                    if(maxPq.isNotEmpty()){
                        val temp=maxPq.poll()
                        hash[temp]=(hash[temp]?:0)-1
                    }
                }
            }else{
                hash[num]=(hash[num]?:0)+1
                minPq.add(num)
                maxPq.add(num)
            }
        }
        while(minPq.isNotEmpty() && hash[minPq.peek()]==0){
            minPq.poll()
        }
        while(maxPq.isNotEmpty() && hash[maxPq.peek()]==0){
            maxPq.poll()
        }
        val min=if(minPq.isNotEmpty()) minPq.peek() else 0
        val max=if(maxPq.isNotEmpty()) maxPq.peek() else 0
        return intArrayOf(max,min)
    }
}