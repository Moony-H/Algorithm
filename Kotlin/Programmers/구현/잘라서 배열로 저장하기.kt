class Solution {
    fun solution(s: String, n: Int) =
        s.map{it.toString()}
            .foldIndexed(listOf<String>()){i,acc,e-> if(i%n==0) acc+listOf(" ")+listOf(e) else acc+listOf(e)}
            .joinToString("").split(" ").filter{it.isNotBlank()}
}