import kotlin.math.pow


fun main() {
    val input = readln().split(" ")
    val n = input[0]
    val b = input[1].toDouble()

    var answer = 0.0
    n.forEachIndexed { index, num ->
        val v = num.toString().toIntOrNull() ?: ((num.code - 'A'.code) + 10)
        answer += b.pow(n.length - index - 1) * v
    }
    println(answer.toLong())


}