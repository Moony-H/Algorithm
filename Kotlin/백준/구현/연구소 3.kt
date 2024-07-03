package org.example

fun <T> combination(
    originList: ArrayList<T>,
    resultList: ArrayList<ArrayList<T>>,
    pickNum: Int,
    picked: ArrayList<T> = arrayListOf(),
    index: Int = 0
) {
    if (pickNum <= 0) {
        resultList.add(ArrayList(picked))
        return
    }
    for (i in index until originList.size - pickNum + 1) {
        picked.add(originList[i])
        combination(originList, resultList, pickNum - 1, picked, i + 1)
        picked.removeLast()
    }

}

//-1: 벽
//MAX: 빈공간

fun copyDeep(table: ArrayList<ArrayList<Int>>): ArrayList<ArrayList<Int>> {
    val result = arrayListOf<ArrayList<Int>>()
    table.forEach {
        val temp = ArrayList<Int>()
        it.forEach { num ->
            temp.add(num)
        }
        result.add(temp)
    }
    return result
}

fun getMax(table: ArrayList<ArrayList<Int>>): Int {
    var result = 0
    table.forEach {
        it.forEach { num ->
            result = if (result < num) num else result
        }
    }
    return result
}


fun bfs(table: ArrayList<ArrayList<Int>>, positions: ArrayList<ArrayList<Int>>) {
    //위치 시간
    val q = ArrayDeque<Pair<ArrayList<Int>, Int>>()
    val UDLR = arrayOf(arrayOf(0, -1), arrayOf(0, 1), arrayOf(-1, 0), arrayOf(1, 0))

    positions.forEach {
        q.addLast(Pair(it, 0))
    }
    while (q.isNotEmpty()) {
        val temp = q.removeFirst()
        val position = temp.first
        val sec = temp.second
        UDLR.forEach {
            val newX = position[0] + it[0]
            val newY = position[1] + it[1]
            if (newX !in table[0].indices || newY !in table.indices)
                return@forEach
            if (table[newY][newX] == -1)
                return@forEach

            val nextSec = table[newY][newX]

            if (nextSec == 0) {
                //검사 안하게 벽으로 막아버림
                table[newY][newX] = -1
                q.addLast(Pair(arrayListOf(newX, newY), sec + 1))
                return@forEach
            }
            if (nextSec <= sec + 1)
                return@forEach

            table[newY][newX] = sec + 1
            q.addLast(Pair(arrayListOf(newX, newY), sec + 1))
        }
    }
}

fun main() {
    val input = readln().split(" ").map { it.toInt() }
    val n = input[0]
    val pickNum = input[1]
    val table = arrayListOf<ArrayList<Int>>()
    repeat(n) {
        table.add(readln().split(" ").map { it.toInt() }.toCollection(ArrayList()))
    }
    val virus = ArrayList<ArrayList<Int>>()
    table.forEachIndexed { y, list ->
        list.forEachIndexed { x, num ->
            //일단 다르게 초기화
            if (num == 0)
                table[y][x] = Int.MAX_VALUE
            //벽
            else if (num == 1)
                table[y][x] = -1
            //바이러스
            if (num == 2) {
                table[y][x] = 0
                virus.add(arrayListOf(x, y))
            }
        }
    }

    val comb = arrayListOf<ArrayList<ArrayList<Int>>>()
    combination(virus, comb, pickNum)
    var answer = Int.MAX_VALUE
    comb.forEach {
        val tempTable = copyDeep(table)
        bfs(tempTable, it)

        val num = getMax(tempTable)
        answer = if (answer > num) num else answer
    }
    println(if (answer == Int.MAX_VALUE) -1 else answer)

}