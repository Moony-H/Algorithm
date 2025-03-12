class Solution {
    fun solution(n: Int, s: IntArray, l: IntArray) =
    when(n){
        1-> l.sliceArray(0..s[1])
        2-> l.sliceArray(s[0] until l.size)
        3-> l.sliceArray(s[0]..s[1])
        else-> l.slice(s[0]..s[1] step s[2])
    }
}