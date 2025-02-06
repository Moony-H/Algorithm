class Solution {
    fun solution(l: IntArray)=l.sorted().slice(5 until l.size).toIntArray()
}