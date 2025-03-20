class Solution {
    fun solution(arr: IntArray, query: IntArray) =
        query.foldIndexed(arr.toList()){i,acc,e-> 
            if(i%2==0) acc.slice(0..e) else acc.slice(e until acc.size)
        }
}