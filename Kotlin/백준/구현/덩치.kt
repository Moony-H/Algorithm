fun main() {
    val person = arrayListOf<Pair<Int, Int>>()
    for (i in 0 until readln().toInt()) {
        val input = readln().split(" ").map { it.toInt() }
        person.add(input[0] to input[1])
    }
    val result = Array(person.size) { 1 }
    person.forEachIndexed { i, p ->
        for (j in 0 until person.size) {
            if (j == i)
                continue
            val p2 = person[j]
            if (p.first <p2.first && p.second < p2.second)
                result[i] +=1
        }
    }
    println(result.joinToString(" "))
}