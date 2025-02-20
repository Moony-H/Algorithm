class Solution {
    fun solution(arr: IntArray) =
        arr.map{
            var temp=it
            var count=-1
            var change=it
            do{
                count++
                temp=change
                change=if(temp>=50 && temp%2==0)
                    temp shr 1
                else if(temp<50 && temp%2!=0)
                    (temp shl 1)+1
                else
                    temp
            }while(temp!=change)
            count
        }.maxOf{it}
}