class Solution {
    fun solution(array: IntArray, commands: Array<IntArray>): IntArray {
        var answer = ArrayList<Int>()
        
        commands.forEach{
            val i=it[0]
            val j=it[1]
            val k=it[2]
            val sub=array.toCollection(ArrayList<Int>()).subList(i-1,j)
            sub.sort()
            answer.add(sub[k-1])
        }
        return answer.toIntArray()
    }
}