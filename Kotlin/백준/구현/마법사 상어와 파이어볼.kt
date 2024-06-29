package org.example


val dir = arrayOf(
    arrayOf(0, -1),
    arrayOf(1, -1),
    arrayOf(1, 0),
    arrayOf(1, 1),
    arrayOf(0, 1),
    arrayOf(-1, 1),
    arrayOf(-1, 0),
    arrayOf(-1, -1)
)
var ballNum = 0

fun generateBallId(): Int = ballNum++

fun getNewFireBalls(balls: ArrayList<FireBall>): Array<FireBall> {
    val mass = balls.sumOf { it.mass } / 5
    val speed = balls.sumOf { it.speed } / balls.size
    val isD = balls.all { it.ballDirection % 2 == 0 }
    val isA = balls.all { it.ballDirection % 2 == 1 }
    val directions = if (isD || isA) arrayOf(0, 2, 4, 6) else arrayOf(1, 3, 5, 7)

    return Array(directions.size) {
        FireBall(mass, balls[0].position.copyOf(), directions[it], speed)
    }
}

fun deleteFireBalls(balls: List<Int>, hash: HashMap<Int, FireBall>) {
    balls.forEach {
        hash.remove(it)
    }
}

data class FireBall(
    val mass: Int,
    val position: Array<Int>,
    val ballDirection: Int,
    val speed: Int
) {
    private val direction: Array<Int> = dir[ballDirection]

    fun move(n: Int) {
        position[0] += direction[0] * speed
        position[1] += direction[1] * speed

        if (position[0] < 0)
            position[0] += (-(position[0] / n) + 1) * n

        if (position[1] < 0)
            position[1] += (-(position[1] / n) + 1) * n

        position[0] %= n
        position[1] %= n
    }
}


fun main() {
    val fireBallHash = HashMap<Int, FireBall>()
    val input = readln().split(" ").map { it.toInt() }
    val n = input[0]
    val m = input[1]
    val k = input[2] //명령 횟수

    val table = Array(n) { Array(n) { HashMap<Int, Boolean>() } }


    for (i in 0 until m) {
        val fireBallInfo = readln().split(" ").map { it.toInt() }
        val y = fireBallInfo[0] - 1
        val x = fireBallInfo[1] - 1
        val mass = fireBallInfo[2]
        val speed = fireBallInfo[3]
        val dirInt = fireBallInfo[4]
        val ball = FireBall(mass, arrayOf(x, y), dirInt, speed)
        val id = generateBallId()
        fireBallHash[id] = ball
        table[y][x][id] = true
    }

    //겜 시작
    for (i in 0 until k) {


        //이동
        fireBallHash.forEach { (t, u) ->
            val x = u.position[0]
            val y = u.position[1]
            table[y][x].remove(t)
            u.move(n)
            val dx = u.position[0]
            val dy = u.position[1]
            table[dy][dx][t] = true
        }

        //파이어볼 검사
        table.forEach { line ->
            line.forEach { hash ->
                if (hash.size >= 2) {
                    val ballsInt = hash.map { it.key }.toCollection(ArrayList())
                    val balls = ballsInt.map { fireBallHash[it]!! }.toCollection(ArrayList())
                    val newBalls = getNewFireBalls(balls)
                    deleteFireBalls(ballsInt, fireBallHash)
                    hash.clear()
                    newBalls.forEach {
                        val id = generateBallId()
                        fireBallHash[id] = it
                        hash[id] = true
                    }
                }
            }
        }

        //0인거 지우기
        fireBallHash.filter { it.value.mass == 0 }.forEach { (t, u) ->
            val x = u.position[0]
            val y = u.position[1]
            table[y][x].remove(t)
            fireBallHash.remove(t)
        }

    }

    var total = 0
    fireBallHash.forEach { t, u ->
        total += u.mass
    }

    println(total)


}
