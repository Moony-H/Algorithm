class Solution {
    fun solution(b: String) =
        b.split(" ").let{
            when(it[1]){
                "+" -> it[0].toInt()+it[2].toInt()
                "-" -> it[0].toInt()-it[2].toInt()
                else -> it[0].toInt()*it[2].toInt()
            }
        }
}