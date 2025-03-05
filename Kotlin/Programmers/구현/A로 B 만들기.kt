class Solution {
    fun solution(b: String, a: String) =
        if(b.toCharArray().sorted() == a.toCharArray().sorted()) 1 else 0
}