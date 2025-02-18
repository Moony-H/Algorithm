class Solution {
    fun solution(names: Array<String>) = 
        names.filterIndexed{i,e-> i%5==0}
}