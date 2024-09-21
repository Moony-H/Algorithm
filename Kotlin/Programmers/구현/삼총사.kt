class Solution {
    
    fun pick(arr:IntArray,start:Int,picked:ArrayList<Int>):Int{
        var answer=0

        if(picked.size>=3)
            return if(picked.sum()==0) 1 else 0
        if(start>=arr.size)
            return 0
        for(i in start until arr.size){
            picked.add(arr[i])
            answer+=pick(arr,i+1,picked)
            picked.removeAt(picked.size-1)
        }
        return answer
    }
    
    fun solution(number: IntArray): Int {
        return pick(number,0,arrayListOf<Int>())
    }
}