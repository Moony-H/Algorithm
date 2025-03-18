class Solution {
    fun solution(str: String, os: String, s: Int) =
        str.substring(0,s)+os+str.substring(s+os.length)
}