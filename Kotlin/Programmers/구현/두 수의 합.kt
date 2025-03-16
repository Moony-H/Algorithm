class Solution {
    fun solution(a: String, b: String)=
        a.padStart(b.length,'0').reversed().zip(b.padStart(a.length,'0').reversed())
        .fold(listOf("","")){acc,e->
            var sum=e.first.toString().toInt()+e.second.toString().toInt()
            if(acc[0].isNotEmpty()) sum+=acc[0].toInt()
            if(sum>=10) listOf("1","${sum.toString()[1]}${acc[1]}")
            else listOf("","$sum${acc[1]}")
        }.joinToString("")
}