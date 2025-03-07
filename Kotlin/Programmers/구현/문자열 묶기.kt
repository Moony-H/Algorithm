class Solution {
    fun solution(arr: Array<String>):Int{
        val hash=hashMapOf<Int,Int>()
        arr.map{it.length}.forEach{
            hash[it]=(hash[it]?:0)+1
        }
        return hash.maxOf{it.value}
    }
}