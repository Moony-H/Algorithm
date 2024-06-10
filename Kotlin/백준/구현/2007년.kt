fun main() {
    val dayOfWeek = arrayOf("SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT")
    val daysOfMonth = arrayOf(31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    val input = readln().split(" ").map { it.toInt() }

    val month = input[0]
    val day = input[1]

    var totalDay = day

    for (i in 0 until month - 1) {
        totalDay += daysOfMonth[i]
    }

    println(dayOfWeek[totalDay % 7])
}