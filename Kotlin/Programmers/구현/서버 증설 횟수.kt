import java.util.*

class Solution {
    fun Queue<Int>.removeServer(i:Int,k:Int):Int{
        var result=0
        while(this.isNotEmpty() && i-this.peek()>=k){
            this.poll()
            result++
        }
        return result
    }
    fun Queue<Int>.addServer(i:Int,num:Int):Int{
        repeat(num){this.add(i)}
        return num
    }
    infix fun Int.sNum(n:Int)=this/n
    
    fun solution(players: IntArray, m: Int, k: Int): Int {
        val servers:Queue<Int> =LinkedList<Int>()
        var serverNum=0
        return players.foldIndexed(0){i,acc,e ->
            serverNum-=servers.removeServer(i,k)
            ((e sNum m)-serverNum).let{
                if(it<0) acc else {
                    serverNum+=servers.addServer(i,it)
                    it+acc
                }
            }
        }
    }
}