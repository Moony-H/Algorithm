package org.example


fun convertLine(arr: ArrayList<Int>): ArrayList<Int> {
    val resultList = ArrayList<ArrayList<Int>>()
    val hash = HashMap<Int, Int>()
    arr.forEach { num ->
        if (num == 0)
            return@forEach
        hash[num]?.let {
            hash[num] = it + 1
        } ?: run {
            hash[num] = 1
        }
    }
    hash.forEach { (t, u) ->
        resultList.add(arrayListOf(t, u))
    }
    return ArrayList(resultList.sortedWith(compareBy<ArrayList<Int>> { it[1] }.thenBy { it[0] }).flatten())
}

fun rOperator(table: ArrayList<ArrayList<Int>>): ArrayList<ArrayList<Int>> {
    var maxLength = 0
    val newTable = ArrayList<ArrayList<Int>>()
    table.forEach {
        val line = convertLine(it)
        maxLength = if (maxLength > line.size) maxLength else line.size
        newTable.add(line)
    }
    newTable.forEach {
        for (i in 0 until maxLength - it.size) {
            it.add(0)
        }
    }
    return newTable
}

fun cOperator(table: ArrayList<ArrayList<Int>>): ArrayList<ArrayList<Int>> {
    var maxLength = 0
    val resultTable = ArrayList<ArrayList<Int>>()
    val convertedTable = ArrayList<ArrayList<Int>>()
    for (i in table[0].indices) {
        val line = arrayListOf<Int>()
        for (j in table.indices) {
            line.add(table[j][i])
        }
        val newLine = convertLine(line)
        maxLength = if (maxLength > newLine.size) maxLength else newLine.size
        convertedTable.add(newLine)
    }

    convertedTable.forEach {
        for (i in 0 until maxLength - it.size) {
            it.add(0)
        }
    }
    for (i in 0 until maxLength) {
        val tempList = ArrayList<Int>()
        for (j in 0 until convertedTable.size) {
            tempList.add(convertedTable[j][i])
        }
        resultTable.add(tempList)
    }

    return resultTable
}

fun main() {

    val input = readln().split(" ").map { it.toInt() }
    val r = input[0] - 1
    val c = input[1] - 1
    val k = input[2]
    var table = arrayListOf<ArrayList<Int>>()
    for (i in 0 until 3) {
        table.add(readln().split(" ").map { it.toInt() }.toCollection(ArrayList()))
    }


    for (i in 0 until 101) {
        if (table.size > r && table[0].size > c && table[r][c] == k) {
            println(i)
            return
        }
        table = if (table.size >= table[0].size) {
            rOperator(table)
        } else {
            cOperator(table)
        }
    }

    println(-1)

}