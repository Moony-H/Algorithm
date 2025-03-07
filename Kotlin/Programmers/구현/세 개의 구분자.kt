class Solution {
    fun solution(s: String):List<String>{
        val answer=s.split("a","b","c").filter{it.isNotBlank()}
        return if(answer.isEmpty()) listOf("EMPTY") else answer
    }
}