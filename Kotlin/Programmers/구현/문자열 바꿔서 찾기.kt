class Solution {
    fun solution(myString: String, pat: String) =
        if(pat in myString.map{if(it=='A') "B" else "A"}.joinToString(""))
            1
        else
            0
}