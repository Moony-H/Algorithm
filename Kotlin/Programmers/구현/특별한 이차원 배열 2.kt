class Solution {
    fun solution(arr: Array<IntArray>) =
        if(List(arr.size){i-> List(arr.size-i){j-> listOf(i,j+i)}}.flatten()
            .all{(i,j)-> arr[i][j]==arr[j][i]}) 1 else 0
}