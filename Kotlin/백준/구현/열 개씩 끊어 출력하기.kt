fun main() {
    val n = readln()
    n.forEachIndexed{index,word->
        if((index+1)%10==0 && index!=0)
            println(word)
        else
            print(word)
    }
}