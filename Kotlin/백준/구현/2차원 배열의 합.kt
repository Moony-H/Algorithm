
fun main() {

    fun sum(i: Int, j: Int, x: Int, y: Int, list: ArrayList<List<Int>>): Int {
        var result = 0
        for (ii in i - 1 until x) {
            for (jj in j - 1 until y) {
                result += list[ii][jj]
            }
        }
        return result
    }

    val n = readln().split(" ").map {
        it.toInt()
    }[0]
    val list = ArrayList<List<Int>>()
    for (i in 0 until n) {
        val l = readln().split(" ").map { it.toInt() }
        list.add(l)
    }

    val k = readln().toInt()
    val results=ArrayList<Int>()
    for (i in 0 until k) {
        val input = readln().split(" ").map {
            it.toInt()
        }
        results.add(sum(input[0], input[1], input[2], input[3], list))
    }
    results.forEach {
        println(it)
    }
}