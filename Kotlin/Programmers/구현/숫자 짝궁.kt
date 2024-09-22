class Solution {
    fun solution(X: String, Y: String): String {
        var answer: String = ""
        val xHash=hashMapOf<String,Int>()
        val yHash=hashMapOf<String,Int>()
        X.forEach{
            xHash[it.toString()]=(xHash[it.toString()]?:0)+1
        }
        Y.forEach{
            yHash[it.toString()]=(yHash[it.toString()]?:0)+1
        }
        xHash.keys.forEach{
            if(!yHash.contains(it))
                return@forEach
            val min=if((xHash[it]?:0)>(yHash[it]?:0)) yHash[it]?:0 else xHash[it]?:0
            answer+=it.repeat(min)
        }
        answer=answer.toCharArray().sortedDescending().joinToString("")
        return if(answer.isEmpty()){
            "-1"
        }else if(answer.all{it=='0'}){
            "0"
        }else{
            answer
        }
    }
}