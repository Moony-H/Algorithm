package org.example

import java.util.PriorityQueue

fun main() {
    val diff = 'a'.code - 'A'.code
    val word = readln()
    val hash = HashMap<Int, Int>()
    word.forEach { c ->
        val temp = c.code
        val cInt = if (temp >= 'a'.code) temp - diff else temp
        hash[cInt]?.let {
            hash[cInt] = it + 1
        } ?: run {
            hash[cInt] = 1
        }
    }
    val l = hash.toList().sortedBy { (k, v) -> -v }
    if(l.size>=2 && l[0].second==l[1].second){
        println("?")
    }else{
        println(l[0].first.toChar())
    }
}