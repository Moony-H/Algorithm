
fun main() {
    readln()
    val list=readln().split(" ").map {
        it.toInt()
    }
    val n=readln().toInt()
    println(list.count { it==n })
}