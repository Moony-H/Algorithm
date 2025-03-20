class Solution {
    fun solution(quiz: Array<String>) =
        quiz.map{q->q.split(" = ").let{s->
                s[0].split(" ").let{if(it[1]=="-") it[0].toInt()-it[2].toInt()
                        else it[0].toInt()+it[2].toInt()} == s[1].toInt()
            }
        }.map{if(it) "O" else "X"}
}