import kotlin.math.*

class Solution {
    fun solution(numbers: IntArray, hand: String): String {
        var answer = ""
        var l=IntArray(2)
        var r=IntArray(2)
        l[0]=3
        l[1]=0
        r[0]=3
        r[1]=2
        //*==10, #==11
        val key=arrayOf(
            arrayOf(3,1),arrayOf(0,0),arrayOf(0,1),arrayOf(0,2),
            arrayOf(1,0),arrayOf(1,1),arrayOf(1,2),
            arrayOf(2,0),arrayOf(2,1),arrayOf(2,2),
            arrayOf(3,0),arrayOf(3,2)
        )
        
        numbers.forEach{
            if(it==1 || it==4 || it==7){
                answer+="L"
                l[0]=key[it][0]
                l[1]=key[it][1]
                return@forEach
            }
            if(it==3 || it==6 || it==9){
                answer+="R"
                r[0]=key[it][0]
                r[1]=key[it][1]
                return@forEach
            }
            val lD=abs(l[0]-key[it][0])+abs(l[1]-key[it][1])
            val rD=abs(r[0]-key[it][0])+abs(r[1]-key[it][1])
            if(lD<rD){
                answer+="L"
                l[0]=key[it][0]
                l[1]=key[it][1]
            }
            else if(rD<lD){
                answer+="R"
                r[0]=key[it][0]
                r[1]=key[it][1]
            }
            else{
                if(hand=="left"){
                    answer+="L"
                    l[0]=key[it][0]
                    l[1]=key[it][1]
                }
                else{
                    answer+="R"
                    r[0]=key[it][0]
                    r[1]=key[it][1]
                }
            }
            
        }
        return answer
    }
}