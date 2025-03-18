class Solution {
    fun solution(i: Array<String>, b: IntArray) =
        i.fold(listOf(0,0)){acc,e->
            val t=acc.toMutableList()
            when(e){
                "left"->{t[0]-=1}
                "right"->{t[0]+=1}
                "up"->{t[1]+=1}
                else->{t[1]-=1}
            }
            if(t[0] in ((-b[0]/2)..(b[0]/2)) && t[1] in ((-b[1]/2)..(b[1]/2))) t else acc   
        }
}