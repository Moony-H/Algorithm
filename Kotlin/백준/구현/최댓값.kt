fun main() {
    val table = ArrayList<List<Int>>()
    for (i in 0 until 9)
        table.add(readln().split(" ").map { it.toInt() })
    var max=0
    var x=0
    var y=0
    for(i in 0 until 9){
        for(j in 0 until 9){
            val value=table[i][j]
            if(max< value){
                y=j+1
                x=i+1
                max=value
            }
        }
    }

    println(max)
    println("$x $y")

}