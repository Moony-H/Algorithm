class Solution {
    fun List<Int>.pad(k:Int)= if(this.size>=k) this else this+List(k-this.size){-1}
    fun solution(arr: IntArray, k: Int) =
        arr.fold(listOf<Int>()){acc,e-> if(e in acc) acc else acc+listOf(e)}
            .pad(k).slice(0 until k)
}