class Solution {
    fun solution(arr: IntArray, n: Int) =
        arr.mapIndexed{i,e->
            if(arr.size%2==0 && i%2!=0)
                e+n
            else if(arr.size%2!=0 && i%2==0)
                e+n
            else
                e
        }.toIntArray()
}