class Solution {
    fun solution(spell: Array<String>, dic: Array<String>) =
        if(dic.any{spell.all{c-> c in it}}) 1 else 2
}