package org.example

val direction = arrayOf(
    Pos(1, 0),
    Pos(0, -1),
    Pos(-1, 0),
    Pos(0, 1),
)

data class Pos(
    var x: Int,
    var y: Int
) {
    operator fun plus(other: Pos) {
        this.x += other.x
        this.y += other.y
    }
}

fun getDragonCurveDirInt(gen: Int, startDir: Int, result: ArrayList<Int> = arrayListOf()): ArrayList<Int> {
    if (result.isEmpty()) result.add(startDir)
    if (gen == 0) return result
    for (i in result.size - 1 downTo 0) {
        result.add((result[i] + 1) % 4)
    }
    return getDragonCurveDirInt(gen - 1, startDir, result)
}

fun getDir(gen: Int, startDir: Int): Array<Pos> {
    val curveInt = getDragonCurveDirInt(gen, startDir)
    return Array(curveInt.size) {
        direction[curveInt[it]]
    }
}


fun main() {
    val table = Array(101) { Array(101) { 0 } }
    val n = readln().toInt()
    repeat(n) {
        val input = readln().split(" ").map { it.toInt() }
        var x = input[0]
        var y = input[1]
        val d = input[2]
        val gen = input[3]
        val dirs = getDir(gen, d)
        table[y][x] = 1
        dirs.forEach {
            x += it.x
            y += it.y
            table[y][x] = 1
        }
    }
    var answer=0
    for (i in 0 until 100) {
        for (j in 0 until 100) {
            if (table[i][j] == 1 && table[i][j + 1] == 1 && table[i + 1][j] == 1 && table[i + 1][j + 1] == 1)
                answer++
        }
    }

    println(answer)
}