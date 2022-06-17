import java.io.*
import java.math.*
import java.security.*
import java.text.*
import java.util.*
import java.util.concurrent.*
import java.util.function.*
import java.util.regex.*
import java.util.stream.*
import kotlin.collections.*
import kotlin.comparisons.*
import kotlin.io.*
import kotlin.jvm.*
import kotlin.jvm.functions.*
import kotlin.jvm.internal.*
import kotlin.ranges.*
import kotlin.sequences.*
import kotlin.text.*

/*
 * Complete the 'hourglassSum' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts 2D_INTEGER_ARRAY arr as parameter.
 */

fun hourglassSum(arr: Array<Array<Int>>): Int {
    var result=-999999
    val hourglass=arrayOf(
        arrayOf(0,0), arrayOf(0,1), arrayOf(0,2),
        arrayOf(1,1),
        arrayOf(2,0),arrayOf(2,1),arrayOf(2,2)
        )
    for(i in 0 until arr.size-2){
        for(j in 0 until arr[i].size-2){
            var sum=0
            hourglass.forEach{
                val dx=j+it[1]
                val dy=i+it[0]
                sum+=arr[dy][dx]
            }
            if(result<sum){
                result=sum
            }
            
        }
    }
    return result

}

fun main(args: Array<String>) {

    val arr = Array<Array<Int>>(6, { Array<Int>(6, { 0 }) })

    for (i in 0 until 6) {
        arr[i] = readLine()!!.trimEnd().split(" ").map{ it.toInt() }.toTypedArray()
    }

    val result = hourglassSum(arr)

    println(result)
}