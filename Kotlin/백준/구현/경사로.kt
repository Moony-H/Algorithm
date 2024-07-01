package org.example


data class Bridge(
    val startIndex: Int,
    val endIndex: Int,
    val maxNum: Int,
    val minNUm: Int
)

fun putBridge(arr: ArrayList<Int>, l: Int): ArrayList<Bridge> {
    val result = arrayListOf<Bridge>()
    arr.forEachIndexed { index, num ->

        if (index + 1 >= arr.size)
            return@forEachIndexed

        if (arr[index] > arr[index + 1])
            result.add(Bridge(index + 1, index + l, arr[index], arr[index + 1]))
        else if (arr[index] < arr[index + 1])
            result.add(Bridge(index + 1 - l, index, arr[index + 1], arr[index]))
    }

    return result

}

fun judgeBridge(arr: ArrayList<Bridge>, n: Int): Boolean {
    //없음?
    if (arr.isEmpty())
        return true
    //범위 벗어남?
    val isNotOutOfRange = arr.all { it.startIndex in 0 until n && it.endIndex in 0 until n }
    if(!isNotOutOfRange)
        return false

    //다리 겹침?
    val conflictTest = Array(n) { 0 }
    arr.forEach { bridge: Bridge ->
        val start = bridge.startIndex
        val end = bridge.endIndex
        if (end >= n)
            return false
        for (i in start..end) {
            conflictTest[i] += 1
        }
    }
    conflictTest.forEach {
        if (it >= 2)
            return false
    }


    //두단계 건너 뛰었음?
    arr.forEach {

        if (it.maxNum - it.minNUm >= 2)
            return false
    }
    return true
}

fun main() {
    val input = readln().split(" ").map { it.toInt() }
    val n = input[0]
    val l = input[1]

    val table = ArrayList<ArrayList<Int>>()

    for (i in 0 until n) {
        table.add(readln().split(" ").map { it.toInt() }.toCollection(ArrayList()))
    }

    var result = 0

    //가로부터
    val horizontal = ArrayList<ArrayList<Bridge>>()
    table.forEach {
        horizontal.add(putBridge(it, l))
    }

    result += horizontal.count { judgeBridge(it, n) }


    //세로
    val vertical = ArrayList<ArrayList<Bridge>>()

    for (i in 0 until n) {
        val tempArr = ArrayList<Int>()
        for (j in 0 until n) {
            tempArr.add(table[j][i])
        }
        vertical.add(putBridge(tempArr, l))
    }

    result += vertical.count { judgeBridge(it, n) }


    println(result)

}
