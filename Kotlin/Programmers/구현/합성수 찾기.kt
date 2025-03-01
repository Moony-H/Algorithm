class Solution {
    fun solution(n: Int) =
        List(n){i-> List(i+1){it+1}}
            .filterIndexed{i,e-> i>=3 && e.filter{((i+1)%it)==0}.size>=3}.size
}