
fun flip(i:Int,j:Int,arr:Array<Int>){
    var l=i
    var r=j
    while(l<r){
        val temp=arr[l]
        arr[l]=arr[r]
        arr[r]=temp
        l++
        r--
    }
}
fun main() {
    val input=readln().split(" ").map { it.toInt() }
    val n=input[0]
    val m=input[1]
    val arr=Array(n){ it+1 }
    for(k in 0 until m){
        val flipInput= readln().split(" ").map { it.toInt() }
        val i=flipInput[0]
        val j=flipInput[1]
        flip(i-1,j-1,arr)
    }
    println(arr.joinToString(" "))
}