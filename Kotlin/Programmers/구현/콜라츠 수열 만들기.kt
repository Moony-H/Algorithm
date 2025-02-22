class Solution {
    fun solution(n: Int)=mutableListOf<Int>(n).apply{
        while(this.last()!=1){
            val l=last()
            add(if(l%2==0) l/2 else l*3+1)
        }
    }
}