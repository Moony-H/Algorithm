class Solution {
    fun solution(code: String) =
        code.foldIndexed(("" to 0)){i,acc,e -> 
            if(e=='1') Pair(acc.first, acc.second xor 1)
            else if(i%2==acc.second) (acc.first+e to acc.second)
            else acc
        }.first.let{if(it.isEmpty()) "EMPTY" else it }
}