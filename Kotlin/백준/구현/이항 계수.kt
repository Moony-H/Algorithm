package org.example

fun fac(n:Int):Int{
    var result=1
    for(i in 2..n){
        result*=i
    }
    return result
}

fun main() {
    val input=readln().split(" ").map { it.toInt() }
    val n=input[0]
    val k=input[1]
    println(fac(n)/ (fac(n-k)* fac(k)))
}