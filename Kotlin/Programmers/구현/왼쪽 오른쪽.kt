class Solution {
    fun solution(list: Array<String>): List<String> {
        var l=list.indexOf("l")
        var r=list.indexOf("r")
        l=if(l<0) 21 else l
        r=if(r<0) 21 else r
        if(l==21 && r==21) return listOf()
        return if(l>r) list.slice(r+1 until list.size) else list.slice(0 until l)
    }
}