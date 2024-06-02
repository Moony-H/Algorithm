fun main() {
    val string = readln()
    val hash = HashMap<Int, Int>()
    string.map {
        it.toString().toInt()
    }.forEach { int ->
        val temp = if (int == 9) 6 else int
        hash[temp]?.let {
            hash[temp] = it + 1
        } ?: run {
            hash[temp] = 1
        }
    }
    hash[6]?.let { hash[6]=it/2+(it%2) }
    var answer=0
    hash.forEach { k, v ->
        answer= if(v>answer) v else answer
    }
    println(answer)

}