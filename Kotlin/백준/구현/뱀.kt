fun main() {

    fun setPos(map: Array<Array<Int>>, pos: Pair<Int, Int>, setInt: Int) {
        map[pos.second][pos.first] = setInt
    }
    val dir = arrayOf(1 to 0, 0 to 1, -1 to 0, 0 to -1)

    val n = readln().toInt()
    val map = Array(n) { Array(n) { 0 } }
    val turn = hashMapOf<Int, Int>()
    for (i in 0 until readln().toInt()) {
        val pos = readln().split(" ").map {
            it.toInt()
        }
        map[pos[0]-1][pos[1]-1] = 1
    }

    for (i in 0 until readln().toInt()) {
        val input = readln().split(" ")
        turn[input[0].toInt()] = if (input[1] == "D") 1 else -1
    }

    val snake = arrayListOf(0 to 0)
    var dirIndex = 0
    var i = 1
    var pos = 0 to 0
    setPos(map, pos, -1)
    while (true) {


        val next = dir[dirIndex]
        pos = pos.first + next.first to pos.second + next.second
        if (pos.first < 0 || pos.second < 0 ||
            pos.first >= map[0].size || pos.second >= map.size ||
            map[pos.second][pos.first] == -1
        )
            break
        snake.add(pos)
        turn[i]?.let {
            dirIndex += it
            if(dirIndex<0) dirIndex=3
            dirIndex%=4
        }
        if (map[pos.second][pos.first] == 1) {
            setPos(map, pos, -1)
            i++
            continue
        }
        setPos(map, pos, -1)
        val last = snake.removeFirst()
        setPos(map,last,0)
        i++
    }
    println(i)
}