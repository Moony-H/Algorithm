class Solution {
    
    fun isPair(a:String, b:String):Boolean = (a=="[" && b=="]") || (a=="(" && b==")") || (a=="{" && b=="}")
    
    fun isCollect(s:String):Boolean{
        val stack=arrayListOf<String>()
        s.forEach{
            stack.add(s.toString())
            while(stack.size>=2 && isPair(stack[stack.size-1],stack[stack.size-2])){
                stack.removeAt(stack.size-1)
                stack.removeAt(stack.size-1)
            }
                
        }
        println("collect: $s ${stack.isEmpty()}")
        return stack.isEmpty()
    }
    fun solution(s: String): Int {
        var answer: Int = 0
        val sString=s.map{it.toString()}.toMutableList()
        answer+=if(isCollect(s)) 1 else 0
        for(i in 0 until sString.size-1){
            val temp=sString.removeAt(0)
            sString.add(temp)
            answer+=if(isCollect(sString.joinToString())) 1 else 0
        }
        return answer
    }
}