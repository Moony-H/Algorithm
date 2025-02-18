class Solution {
    fun solution(l: IntArray) =
        l.filterIndexed{i,e-> (i+1)%2!=0}.sum().let{
            val temp=l.filterIndexed{i,e-> (i+1)%2==0}.sum()
            if(temp>it)
                temp
            else
                it
        }
}