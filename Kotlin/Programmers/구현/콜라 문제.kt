class Solution {
    fun solution(a: Int, b: Int, n: Int): Int {
        var answer: Int = 0
        var remain=n
        while(remain/a!=0){
            answer+=b*(remain/a)
            remain=b*(remain/a)+remain%a
        }
        return answer
    }
}