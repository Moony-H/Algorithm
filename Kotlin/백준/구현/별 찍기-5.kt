fun main() {
    val n = readln().toInt()
    for (i in 0 until n) {
        val space = ((1+n*2) / 2) - 1 - i
        val star=1+i*2
        println(" ".repeat(space)+"*".repeat(star))
    }
}