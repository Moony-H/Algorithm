package org.example


fun main() {

    val n = readln().toInt()
    val list = readln().split(" ").map { it.toInt() }
    val input = readln().split(" ").map { it.toInt() }
    val b = input[0]
    val c = input[1]

    var answer = 0

    for (i in 0 until n) {
        val num = list[i] - b
        answer += 1
        if (num <= 0)
            continue
        answer += num / c
        if(num%c!=0)
            answer+=1

    }

    println(answer)
}