fun main() {
    var totalPoint = 0f
    var total = 0f
    val hash = hashMapOf(
        "A+" to 4.5f, "A0" to 4.0f, "B+" to 3.5f,
        "B0" to 3.0f, "C+" to 2.5f, "C0" to 2.0f, "D+" to 1.5f, "D0" to 1.0f, "F" to 0f
    )
    for (i in 0 until 20) {

        val input = readln().split(" ")
        val point = input[1].toFloat()
        val grade = input[2]
        if (grade == "P")
            continue
        totalPoint += point
        total += point * hash[grade]!!
    }
    println(String.format("%.6f", total / totalPoint))
}