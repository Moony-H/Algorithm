class Solution {
    fun solution(strArr: Array<String>) =
        strArr.mapIndexed{i,e-> if(i%2==0) e.lowercase() else e.uppercase()}
}