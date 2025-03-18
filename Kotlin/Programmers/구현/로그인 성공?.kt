class Solution {
    fun solution(id_pw: Array<String>, db: Array<Array<String>>):String{
        val hash=hashMapOf(0 to "fail", 1 to "wrong pw", 2 to "login")
        val t=db.map{when{
            id_pw[0]==it[0] && id_pw[1]==it[1] -> 2
            id_pw[0]==it[0] ->1
            else -> 0
        }}.maxOf{it}
        return hash[t]!!
    }
}