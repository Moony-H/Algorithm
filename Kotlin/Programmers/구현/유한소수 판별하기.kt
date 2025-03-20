class Solution {
    fun Int.is25():Int{
        var n=this
        while(n%2==0) n/=2
        while(n%5==0) n/=5
        return if(n==1) 1 else 2
    }
    fun gcd(a:Int,b:Int):Int= if(b==0) a else gcd(b,a%b)
    fun solution(a: Int, b: Int) = (b/gcd(a,b)).is25()
}