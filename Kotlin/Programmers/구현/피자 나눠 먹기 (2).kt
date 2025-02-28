class Solution {
    fun gcd(a: Int, b:Int):Int = if(b != 0) gcd(b, a % b) else a
    fun solution(n: Int)= (n*6)/(gcd(6,n)*6)
}