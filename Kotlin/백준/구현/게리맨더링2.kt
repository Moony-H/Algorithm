package org.example


fun divideTable(table: List<List<Int>>, x: Int, y: Int, d1: Int, d2: Int): List<List<Int>>? {
    val copyTable = ArrayList<ArrayList<Int>>()
    table.forEach {
        val temp = ArrayList<Int>()
        it.forEach { _ ->
            temp.add(-1)
        }
        copyTable.add(temp)
    }

    for (i in 0..d1) {
        val newX = x - i
        val newY = y + i
        if (newX !in table[0].indices || newY !in table.indices)
            return null
        copyTable[newY][newX] = 5

        val newX2 = x + d2 - i
        val newY2 = y + d2 + i
        if (newX2 !in table[0].indices || newY2 !in table.indices)
            return null
        copyTable[newY2][newX2] = 5

    }
    for (i in 0..d2) {
        val newX = x + i
        val newY = y + i
        if (newX !in table[0].indices || newY !in table.indices)
            return null
        copyTable[newY][newX] = 5

        val newX2 = x - d1 + i
        val newY2 = y + d1 + i
        if (newX2 !in table[0].indices || newY2 !in table.indices)
            return null
        copyTable[newY2][newX2] = 5
    }


    for (i in table.indices) {
        var start = -1
        var end = -1
        for (j in table.indices) {
            if (copyTable[i][j] == 5 && start == -1) {
                start = j
                continue
            }
            if (copyTable[i][j] == 5 && end == -1) {
                end = j
                continue
            }
        }
        if (start != -1 && end != -1) {
            for (k in start..end) {
                copyTable[i][k] = 5
            }
        }
    }


    for (i in 0 until copyTable.size) {
        for (j in 0 until copyTable[i].size) {
            if (copyTable[i][j] != -1)
                continue
            copyTable[i][j] = if (i in 0 until (y + d1) && j in 0..x)
                1
            else if (i in 0..y + d2 && (j > x && j < copyTable[i].size))
                2
            else if (i in y + d1 until copyTable.size && j in 0 until (x - d1 + d2))
                3
            else if ((i > y + d2 && i < copyTable.size) && j in (x - d1 + d2) until table[i].size)
                4
            else 5
        }
    }




    return copyTable
}

fun countPeople(table: List<List<Int>>, copyTable: List<List<Int>>): HashMap<Int, Int> {
    val hash = hashMapOf<Int, Int>()

    for (i in table.indices) {
        for (j in table[i].indices) {
            val area = copyTable[i][j]
            hash[area] = (hash[area] ?: 0) + table[i][j]
        }
    }

    return hash
}


fun main() {
    val n = readln().toInt()
    val table = ArrayList<ArrayList<Int>>()
    repeat(n) {
        table.add(readln().split(" ").map { it.toInt() }.toCollection(ArrayList()))
    }

    var result = Int.MAX_VALUE

    for (y in 1 until n) {

        for (x in 1 until n) {
            for (d1 in 1 until n) {
                for (d2 in 1 until n) {
                    var max = 0
                    var min = Int.MAX_VALUE
                    val divideTable = divideTable(table, x, y, d1, d2) ?: continue
                    val hash = countPeople(table, divideTable)
                    hash.forEach { t, u ->
                        if (max < u)
                            max = u
                        if (min > u)
                            min = u
                    }
                    if (result > max - min)
                        result = max - min

                }
            }
        }
    }



    println(result)
}