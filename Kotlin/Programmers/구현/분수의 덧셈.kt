class Solution {
    infix fun Int.gcd(a:Int):Int = if(a==0) this else a gcd (this % a)
    infix fun Int.lcm(a:Int):Int= (this/(this gcd a)) * a
    fun solution(n1: Int, d1: Int, n2: Int, d2: Int) =
        (d1 lcm d2).let{l-> 
            val n=(l/d1)*n1+(l/d2)*n2
            (n gcd l).let{listOf(n/it,l/it)}
        }    
}