class Solution {
    fun solution(numbers: IntArray, n: Int) = 
        numbers.reduce{ acc,e -> if(acc>n) acc else acc+e}
}