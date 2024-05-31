fun main() {
    val arr=IntArray(10001)
    for(i in 1..10000){
        var n=i
        while(n<10001){
            arr[n]+=1
            if(arr[n]>=2)
                break
            n += n.toString().sumOf {
                it.code - 48
            }
        }
    }
    arr.forEachIndexed {index,n->
        if(n==1) println(index)
    }
}