class Solution {
    fun solution(s: String): IntArray {
        var answer= ArrayList<Int>()
        val hash=HashMap<Char,Int>()
        s.forEachIndexed{index,char->
            hash[char]?.let{
                answer.add(index-it)
            }?:run{
                answer.add(-1)
            }
            hash[char]=index
        }
        return answer.toIntArray()
    }
}