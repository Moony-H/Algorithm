class Solution {
    fun solution(n: Int, s: IntArray, l: IntArray) =
    when(n){
        1-> l.slice(0..s[1]).toList()
        2-> l.slice(s[0] until s.size).toList()
        3-> l.slice(s[0]..s[1]).toList()
        else-> l.slice(s[0]..s[1]).filterIndexed{i,e-> (i+1)%s[2]!=0}
    }
}