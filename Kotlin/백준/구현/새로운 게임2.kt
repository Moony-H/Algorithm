package org.example

import java.util.Stack


fun <T> Stack<T>.popUntil(item: T): ArrayList<T> = ArrayList<T>().apply {
    while (peek() != item) {
        add(pop())
    }
    add(pop())
}

fun <T> Stack<T>.popAll(): ArrayList<T> = ArrayList<T>().apply {
    while (this@popAll.isNotEmpty()) {
        add(pop())
    }
}

data class Position(
    var x: Int,
    var y: Int
) {
    operator fun minus(other: Position): Position = Position(this.x - other.x, this.y - other.y)
    operator fun plus(other: Position): Position = Position(this.x + other.x, this.y + other.y)


    fun reverse() {
        this.x = -this.x
        this.y = -this.y
    }

    override fun toString(): String = "x: $x y: $y"
}

enum class SpaceType {
    WHITE, RED, BLUE
}

data class Space(
    val type: SpaceType,
) {
    val stack = Stack<ChesPiece>()

    fun popUntil(chesPiece: ChesPiece): ArrayList<ChesPiece> =
        stack.popUntil(chesPiece)
}


class ChesPiece(val num: Int, val dir: Position, var position: Position) {

    val x: Int
        get() = position.x
    val y: Int
        get() = position.y


    fun next() = position + dir

    fun reverseDir() {
        dir.reverse()
    }

    override fun equals(other: Any?): Boolean = (other is ChesPiece) && this.num == other.num
    override fun hashCode(): Int {
        var result = num
        result = 31 * result + dir.hashCode()
        result = 31 * result + position.hashCode()
        return result
    }
}

fun getDir(dirInt: Int): Position = when (dirInt) {
    1 -> Position(1, 0)
    2 -> Position(-1, 0)
    3 -> Position(0, -1)
    4 -> Position(0, 1)
    else -> throw IllegalStateException("dir int not found")
}

fun main() {
    val input = readln().split(" ").map { it.toInt() }
    val n = input[0]
    val k = input[1]
    val table = ArrayList<List<Space>>()
    for (i in 0 until n) {
        table.add(readln().split(" ").map {
            Space(SpaceType.entries[it.toInt()])
        })
    }

    val chesList = ArrayList<ChesPiece>()
    for (i in 0 until k) {
        val chesInput = readln().split(" ").map { it.toInt() }
        chesList.add(ChesPiece(i, getDir(chesInput[2]), Position(chesInput[1] - 1, chesInput[0] - 1)))
    }

    chesList.forEach {
        table[it.y][it.x].stack.push(it)
    }

    for (i in 1 until 1001) {
        chesList.forEach { ches ->
            chesList.forEach {
                val stack = table[it.y][it.x]
                if (stack.stack.size >= 4) {
                    println(i)
                    return
                }
            }

            val nowSpace = table[ches.y][ches.x]
            var next = ches.next()
            if (next.x < 0 || next.x >= n || next.y < 0 || next.y >= n) {
                ches.reverseDir()
                next = ches.next()
            }
            val nextSpace = table[next.y][next.x]
            when (nextSpace.type) {
                SpaceType.WHITE -> {
                    val tempStack = Stack<ChesPiece>()
                    nowSpace.popUntil(ches).forEach {
                        tempStack.push(it)
                    }

                    tempStack.popAll().forEach {
                        it.position = next
                        nextSpace.stack.push(it)
                    }


                }

                SpaceType.RED -> {
                    nowSpace.popUntil(ches).forEach {
                        it.position = next
                        nextSpace.stack.push(it)
                    }
                }

                SpaceType.BLUE -> {
                    ches.reverseDir()
                    val reverseNext = ches.next()
                    if (reverseNext.x in 0 until n && reverseNext.y in 0 until n && table[reverseNext.y][reverseNext.x].type == SpaceType.BLUE) {
                        return@forEach
                    }
                    if(reverseNext.x<0 || reverseNext.y<0 || reverseNext.x>=n || reverseNext.y>=n)
                        return@forEach

                    val reverseNextSpace = table[reverseNext.y][reverseNext.x]
                    when (reverseNextSpace.type) {
                        SpaceType.WHITE -> {
                            val tempStack = Stack<ChesPiece>()
                            nowSpace.popUntil(ches).forEach {
                                tempStack.push(it)
                            }

                            tempStack.popAll().forEach {
                                it.position = reverseNext
                                reverseNextSpace.stack.push(it)
                            }


                        }

                        SpaceType.RED -> {
                            nowSpace.popUntil(ches).forEach {
                                it.position = reverseNext
                                reverseNextSpace.stack.push(it)
                            }
                        }
                        else->{}
                    }


                }
            }

        }
        chesList.forEach {
            val stack = table[it.y][it.x]
            if (stack.stack.size >= 4) {
                println(i)
                return
            }
        }
    }
    println(-1)

}