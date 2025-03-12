class Solution {
    fun solution(n: Int):List<Int>{
        var answer=mutableListOf<Int>()
        var temp=n
        while(temp!=1){
            var mul=2
            while(temp%mul!=0){
                mul++
            }
            temp/=mul
            answer.add(mul)
        }
        return answer.toSet().toList()
    }
}