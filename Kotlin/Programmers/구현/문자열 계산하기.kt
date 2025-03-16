class Solution {
    fun solution(s: String): Int{
        val line=s.split("""(?=[+-])\s*""".toRegex()).map{it.trim()}
        var answer=line[0].toInt()
        for(i in 1 until line.size){
            val c=line[i].split(" ")
            if(c[0]=="+")
                answer+=c[1].toInt()
            else
                answer-=c[1].toInt()
        }
        return answer
    }
}