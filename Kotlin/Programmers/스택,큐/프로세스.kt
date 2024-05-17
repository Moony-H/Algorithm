class Solution {
    
    fun find(a:ArrayDeque<Pair<Int,Int>>,v:Pair<Int,Int>):Int{
        val value=v.second
        a.forEach{item->
            if(value<item.second){
                return item.first
            }
        }
        return v.first
    }
    fun solution(priorities: IntArray, location: Int): Int {
        var answer = 0
        val result=ArrayList<Pair<Int,Int>>()
        val a=ArrayDeque<Pair<Int,Int>>()
        priorities.forEachIndexed{i,item->
            a.add(Pair(i,item))
        }
        
        while(a.size!=0){

            println()
            val i=a.removeFirst()
            val findResult=find(a,i)
            if(findResult==i.first){
                result.add(i)
            }else{
                a.add(i)
            }
        }
        
        result.forEachIndexed{index,item->
            if(item.first==location){
                return index+1
            }
        }
        
        
        return answer
    }
}