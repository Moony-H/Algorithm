import java.util.*

fun main(){
    val a=readLine()!!
    val at=a.split(" ")
    val n=at[0].toInt()
    val m=at[1].toInt()
    val table=Array<Array<Int>>(n){
        Array<Int>(m){
            0
        }
    }
    for(i in 0 until n){
        val temp= readLine()!!
        for(j in temp.indices){
            table[i][j]=temp[j].toString().toInt()
        }
    }

    val s=Solution()
    s.solution(table)
}
class Solution {

    fun solution(graph:Array<Array<Int>>):String{
        val q:Queue<Pair<Int,Int>> = LinkedList<Pair<Int,Int>>()
        q.add(Pair(0,0))
        
        while(q.isNotEmpty()){
            val pos=q.poll()
            val dx=pos.first
            val dy=pos.second
            
        }
        return ""
    }
}