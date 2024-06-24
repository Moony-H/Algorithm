package org.example


enum class RollDir {
    RIGHT, LEFT, UP, DOWN
}

data class Dice(

    //다이스 위치
    var x: Int,
    var y: Int,

    //동, 서, 북, 남
    // 4 방향과 가운데, 그리고 반대편
    var right: Int = 2,
    var left: Int = 3,
    var up: Int = 1,
    var down: Int = 4,
    //반대
    var opposite: Int = 5,
    //현재 위에 있는 면.
    var face: Int = 0,

    )

fun rollDice(dice: Dice, rollDir: RollDir) {
    when (rollDir) {
        RollDir.RIGHT -> {
            dice.run {
                x++
                val oppositeTemp = opposite
                opposite = right
                right = face
                face = left
                left = oppositeTemp
            }
        }

        RollDir.LEFT -> {
            dice.run {
                x--
                val oppositeTemp = opposite
                opposite = left
                left = face
                face = right
                right = oppositeTemp

            }
        }

        RollDir.UP -> {
            dice.run {
                y--
                val oppositeTemp = opposite
                opposite = up
                up = face
                face = down
                down = oppositeTemp
            }
        }

        RollDir.DOWN -> {
            dice.run {
                y++
                val oppositeTemp = opposite
                opposite = down
                down = face
                face = up
                up = oppositeTemp
            }
        }
    }
}

fun main() {


    //면의 숫자.
    val dicePoint = arrayOf(0, 0, 0, 0, 0, 0)

    val input = readln().split(" ").map { it.toInt() }
    val n = input[0]
    val m = input[1]

    val inputY = input[2]
    val inputX = input[3]

    val dice = Dice(inputX, inputY)

    val map = Array(n) { Array(m) { 0 } }

    for (i in 0 until n) {
        readln().split(" ").map { it.toInt() }.forEachIndexed { j, num ->
            map[i][j] = num
        }
    }

    val dirCommand = readln().split(" ").map { it.toInt() - 1 }

    dirCommand.forEach { dirCommandInt ->
        val rollDir = RollDir.entries[dirCommandInt]
        var dx = 0
        var dy = 0
        when (rollDir) {
            RollDir.RIGHT -> {
                dx++
            }

            RollDir.LEFT -> {
                dx--
            }

            RollDir.UP -> {
                dy--
            }

            RollDir.DOWN -> {
                dy++
            }
        }
        val newX = dx + dice.x
        val newY = dy + dice.y

        if (newX >= m || newX < 0 || newY >= n || newY < 0)
            return@forEach

        rollDice(dice, rollDir)

        if (map[dice.y][dice.x] == 0) {
            map[dice.y][dice.x] = dicePoint[dice.opposite]
        } else {
            dicePoint[dice.opposite] = map[dice.y][dice.x]
            map[dice.y][dice.x] = 0
        }
        println(dicePoint[dice.face])

    }


}