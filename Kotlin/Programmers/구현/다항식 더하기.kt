class Solution {
    fun solution(p: String) =
        p.split(" + ").groupBy{if("x" in it) "x" else ""}
            .map{h -> h.value.map{n-> 
                    n.replace(Regex("[^0-9]"),"").let{if(it.isBlank()) 1 else it.toInt()}
                }.sumOf{it}.let{if(it==1 && h.key=="x") "" else it.toString()}+h.key
            }.let{if("x" !in it[0] && it.size>1) listOf(it[1],it[0]) else it}.joinToString(" + ")
}