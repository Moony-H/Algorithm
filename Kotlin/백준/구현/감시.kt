fun Array<Array<Int>>.deepCopy() = Array(size) { get(it).clone() }


class Camera(cameraType: CameraType) {

    val dir: Array<Pair<Int, Int>>
    val case: Int

    init {
        val result=when (cameraType) {
            CameraType.ONE ->Pair(arrayOf(Pair(1, 0)),4)
            CameraType.OPPOSITE -> Pair(arrayOf(Pair(-1, 0), Pair(1, 0)),2)
            CameraType.RIGHT_ANGLE -> Pair(arrayOf(Pair(0, -1), Pair(1, 0)),4)
            CameraType.THREE -> Pair(arrayOf(Pair(0, -1), Pair(1, 0), Pair(-1, 0)),4)
            CameraType.WHOLE -> Pair(arrayOf(Pair(0, 1), Pair(0, -1), Pair(1, 0), Pair(-1, 0)),1)
        }
        dir=result.first
        case=result.second
    }


    private fun rotateOneDir(dir: Pair<Int, Int>): Pair<Int, Int> {
        if (dir.first != 0)
            return Pair(0, -dir.first)
        return Pair(dir.second, 0)
    }

    fun rotateDir() {
        for (i in this.dir.indices) {
            this.dir[i] = rotateOneDir(this.dir[i])
        }
    }
}

enum class CameraType {
    ONE,
    OPPOSITE,
    RIGHT_ANGLE,
    THREE,
    WHOLE
}

fun search(map: Array<Array<Int>>, cameraDir: Pair<Int, Int>, start: Pair<Int, Int>) {
    var x = start.first + cameraDir.first
    var y = start.second + cameraDir.second
    while (x >= 0 && x < map[0].size && y >= 0 && y < map.size) {
        if (map[y][x] == 6)
            break
        if (map[y][x] == 0)
            map[y][x] = -1
        x += cameraDir.first
        y += cameraDir.second

    }
}

fun getNoCameraCount(map: Array<Array<Int>>): Int {
    var result = 0
    map.forEach { line ->
        line.forEach { num ->
            if (num == 0)
                result++
        }
    }
    return result
}


fun getMinimum(map: Array<Array<Int>>, cameraPositions: ArrayList<Pair<Int, Int>>, startIndex: Int): Int {
    var min = 64
    var newMap: Array<Array<Int>>
    if (startIndex >= cameraPositions.size)
        return getNoCameraCount(map)

    val cameraPos = cameraPositions[startIndex]
    val cameraTypeInt = map[cameraPos.second][cameraPos.first] - 1
    val cameraType = CameraType.entries[cameraTypeInt]
    val camera = Camera(cameraType)
    for (i in 0 until camera.case) {
        camera.rotateDir()
        newMap = map.deepCopy()
        camera.dir.forEach {
            search(newMap, it, cameraPos)
        }


        val result = getMinimum(newMap, cameraPositions, startIndex + 1)
        min = if (result < min) result else min

    }
    return min
}


fun main() {
    val nm = readln().split(" ").map { it.toInt() }
    val n = nm[0]

    val map = Array(n) {
        val list = readln().split(" ").map { it.toInt() }
        Array(list.size) { list[it] }
    }
    val cameraPositions = ArrayList<Pair<Int, Int>>()
    map.forEachIndexed { i, line ->
        line.forEachIndexed { j, num ->
            if (num in 1..5)
                cameraPositions.add(Pair(j, i))
        }
    }

    println(getMinimum(map, cameraPositions, 0))

}