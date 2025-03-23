class Solution {
    fun List<List<Int>>.findX(n:Int):Int{
        this.forEach{it.forEachIndexed{j,e-> if(e==n) return j}}
        return -1
    }
    fun solution(n: Int, w: Int, num: Int): Int {
        var nn=n
        var answer=0
        val list=List(n/w+if(n%w==0) 0 else 1){i->
            List(w){if(nn<1) 0 else n-(nn--)+1}.let{if(i%2==0) it else it.reversed()}
        }
        val x= list.findX(num)
        for(i in list.size-1 downTo 0){
            if(list[i][x]==num) return answer+1
            answer+=if(list[i][x]==0) 0 else 1
        }
        return 0
    }
}