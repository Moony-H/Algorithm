fun main() {
    fun swap(array:Array<Int>,i:Int,j:Int){
        val temp=array[i]
        array[i]=array[j]
        array[j]=temp
    }

    val input=readln().split(" ").map{it.toInt()}
    val n=input[0]
    val m=input[1]

    val arr=Array(n){it+1}
    for(k in 0 until m){
        val swapInput=readln().split(" ").map { it.toInt() }
        val i=swapInput[0]-1
        val j=swapInput[1]-1
        swap(arr,i,j)
    }

    println(arr.joinToString(" "))
}