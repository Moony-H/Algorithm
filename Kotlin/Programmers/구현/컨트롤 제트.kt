class Solution {
    fun solution(s: String) =
        s.replace("[0-9]+ Z".toRegex(),"0").split(" ").sumOf{it.toInt()}
}