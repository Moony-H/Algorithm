class Solution {
    fun solution(s: String):List<Int>{
        val hash=HashMap<Char,Int>()
        for(i in 65..90){hash[i.toChar()]=0}
        for(i in 97..122){hash[i.toChar()]=0}
        s.forEach{hash[it]=(hash[it]?:0)+1}
        return hash.map{it.value}
    }
}