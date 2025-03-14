class Solution {
    fun solution(arr: IntArray)=
        arr.fold(listOf<Int>()){acc,e-> if(acc.isEmpty()) listOf(e) else acc.filter{it<e}+listOf(e)}
}