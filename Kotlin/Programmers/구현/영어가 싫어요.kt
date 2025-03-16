class Solution {
    fun solution(n: String) =
        listOf(
            listOf("zero","0"),
            listOf("one","1"),
            listOf("two","2"),
            listOf("three","3"),
            listOf("four","4"),
            listOf("five","5"),
            listOf("six","6"),
            listOf("seven","7"),
            listOf("eight","8"),
            listOf("nine","9"))
            .fold(n){acc,e-> acc.replace(e[0],e[1])}.toLong()
}