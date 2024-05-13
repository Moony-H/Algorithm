
class Solution(){
    fun solution(targets: Array<IntArray>): Int {
        var answer: Int = 0
        targets.sortWith(
            compareBy({it[1]},{it[0]})
        )
        var e=0
        targets.forEach{
            if(it[0]>=e){
                e=it[1]
                answer+=1
            }
        }
        return answer
    }
}