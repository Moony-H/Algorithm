fun checkString(string: String):Boolean{
    for(i in 0 until (string.length/2)+1){
        if(string[i]!=string[string.length-1-i]) return false
    }
    return true
}

fun main() {
    while(true){
        val input=readln()
        if(input=="0")
            return
        println(if(checkString(input))"yes" else "no")
    }
}