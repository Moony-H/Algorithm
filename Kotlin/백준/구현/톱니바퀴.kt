package org.example


data class Gear(
    val teeth: ArrayList<Int>,
) {

    private var rotate = 0

    val right: Int
        get() = teeth[clamp(rotate + 2)]

    val left: Int
        get() = teeth[clamp(rotate - 2)]

    val top: Int
        get() = teeth[clamp(rotate)]

    private fun clamp(num: Int): Int =
        if (num < 0)
            num + ((num / teeth.size) + 1) * teeth.size
        else
            num % teeth.size

    fun move(num: Int) {
        rotate += num
        rotate = clamp(rotate)//??? 왜 이걸 또 해야대?
    }
}

fun main() {
    val gears = ArrayList<Gear>().apply {
        for (i in 0 until 4) {
            val teeth = readln().map { it.toString().toInt() }.toCollection(ArrayList())
            add(Gear(teeth))
        }
    }
    val k = readln().toInt()
    for (i in 0 until k) {
        val input = readln().split(" ").map { it.toInt() }
        val num = input[0] - 1
        val dir = -input[1]

        var numTemp = num
        var dirTemp = -dir
        val haveToChangeList = ArrayList<Pair<Int, Gear>>()
        haveToChangeList.add(Pair(dir, gears[numTemp]))

        //오른쪽 방향 부터
        while (numTemp < 3) {
            if (gears[numTemp].right != gears[numTemp + 1].left) {
                haveToChangeList.add(Pair(dirTemp, gears[numTemp + 1]))
            } else
                break
            dirTemp = -dirTemp
            numTemp++
        }
        numTemp = num
        dirTemp = -dir
        while (numTemp > 0) {
            if (gears[numTemp].left != gears[numTemp - 1].right)
                haveToChangeList.add(Pair(dirTemp, gears[numTemp - 1]))
            else
                break
            dirTemp = -dirTemp
            numTemp--
        }

        //돌리기
        haveToChangeList.forEach {
            val direction = it.first
            val gear = it.second
            gear.move(direction)
        }

    }

    var result = 0
    val points = arrayOf(1, 2, 4, 8)
    gears.forEachIndexed { index, gear ->
        result += gear.top * points[index]
    }

    println(result)

}